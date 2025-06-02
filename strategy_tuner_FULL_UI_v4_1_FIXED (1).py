# strategy_tuner_FULL_UI_v4_1_FIXED.py
# Timestamp: 2025-06-02 03:32:54
# Description: Fixed plotting bug (no numeric data to plot) + UI fully restored

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from hmmlearn.hmm import GaussianHMM
from scipy.signal import welch
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Hurst exponent
def compute_hurst(ts, window=100):
    if len(ts) < window:
        return np.nan
    lags = range(2, 20)
    tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags]
    poly = np.polyfit(np.log(lags), np.log(tau), 1)
    return poly[0]

# Spectral slope
def compute_spectral_slope(ts, fs=1.0):
    if len(ts) < 64:
        return np.nan
    f, Pxx = welch(ts, fs=fs)
    f = f[1:]
    Pxx = Pxx[1:]
    slope, _ = np.polyfit(np.log(f), np.log(Pxx), 1)
    return slope

# Main UI
st.set_page_config(layout="wide")
st.title("📈 Strategy Tuner v4.1 - FIXED")

ticker = st.sidebar.text_input("Ticker", "SPY")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2010-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2024-06-01"))
hurst_threshold = st.sidebar.slider("Hurst Threshold", 0.4, 0.9, 0.55)
spectral_threshold = st.sidebar.slider("Spectral Threshold", -4.0, -0.1, -1.5)
trend_leverage = st.sidebar.slider("Trend Regime Leverage", 0.0, 5.0, 1.0)
chop_leverage = st.sidebar.slider("Chop Regime Leverage", 0.0, 5.0, 0.0)
slippage_pct = st.sidebar.slider("Slippage per Trade (%)", 0.0, 1.0, 0.1)
commission_pct = st.sidebar.slider("Commission per Trade (%)", 0.0, 1.0, 0.02)

df = yf.download(ticker, start=start_date, end=end_date)
if df.empty or 'Close' not in df.columns:
    st.error("No data downloaded. Please check ticker and dates.")
else:
    df = df[['Close']].rename(columns={'Close': 'Price'})
    df['LogReturn'] = np.log(df['Price'] / df['Price'].shift(1))
    df.dropna(inplace=True)

    if len(df) < 250:
        st.warning("Not enough data to proceed. Try increasing date range.")
    else:
        df['Hurst'] = df['Price'].rolling(100).apply(compute_hurst, raw=False)
        df['Spectral'] = df['Price'].rolling(128).apply(compute_spectral_slope, raw=False)
        df.dropna(inplace=True)

        hmm = GaussianHMM(n_components=2, covariance_type="diag", n_iter=1000)
        hmm.fit(df[['LogReturn']])
        hidden_states = hmm.predict(df[['LogReturn']])
        df['Regime'] = hidden_states

        trend_regime = df.groupby('Regime')['LogReturn'].mean().idxmax()
        df['Position'] = 0.0

        for i in range(len(df)):
            if df['Hurst'].iloc[i] > hurst_threshold and df['Spectral'].iloc[i] < spectral_threshold:
                if df['Regime'].iloc[i] == trend_regime:
                    df.at[df.index[i], 'Position'] = trend_leverage
                else:
                    df.at[df.index[i], 'Position'] = chop_leverage

        df['StrategyReturns'] = df['LogReturn'] * df['Position']
        df['Equity'] = (df['StrategyReturns']).cumsum().apply(np.exp)

        if df['Equity'].isnull().all() or df['Equity'].nunique() == 0:
            st.error("Simulation failed: no numeric data to plot. Try adjusting thresholds or expanding the date range.")
        else:
            slippage = (slippage_pct + commission_pct) / 100
            trades = df['Position'].diff().abs().sum()
            equity_adjusted = df['Equity'].iloc[-1] * (1 - slippage) ** trades

            st.subheader("📊 Equity Curve")
            st.line_chart(df['Equity'])

            st.markdown(f"**Total Trades**: {int(trades)}")
            st.markdown(f"**Net Final Equity (slippage-adjusted)**: {equity_adjusted:.2f}")

            sharpe = df['StrategyReturns'].mean() / df['StrategyReturns'].std() * np.sqrt(252)
            st.markdown(f"**Annualized Sharpe Ratio**: {sharpe:.2f}")

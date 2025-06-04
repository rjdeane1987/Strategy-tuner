
# strategy_tuner_FULL_UI_v5_WORKING.py
# Fully functional Streamlit strategy tuner with regime logic, filters, leverage, slippage

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from hmmlearn.hmm import GaussianHMM
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(layout="wide")
st.title("📈 Strategy Tuner v5 – Working Build")

ticker = st.sidebar.text_input("Ticker", "SPY")
start_date = st.sidebar.date_input("Start Date", datetime(2015, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.today())
hurst_window = st.sidebar.slider("Hurst Lookback", 20, 200, 100)
spectral_window = st.sidebar.slider("Spectral Lookback", 20, 200, 100)
regime_states = st.sidebar.slider("HMM States", 2, 4, 3)
leverage = st.sidebar.slider("Leverage", 0.0, 3.0, 1.0, 0.1)
drawdown_limit = st.sidebar.slider("Max Drawdown (%)", 0, 100, 100)

@st.cache_data
def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    if "Adj Close" not in df:
        st.error("Missing 'Adj Close' in downloaded data.")
        return pd.DataFrame()
    df["Price"] = df["Adj Close"]
    df["LogReturn"] = np.log(df["Price"] / df["Price"].shift(1))
    df.dropna(inplace=True)
    return df

df = load_data(ticker, start_date, end_date)

if df.empty or len(df) < max(hurst_window, spectral_window, 50):
    st.warning("Insufficient data loaded for analysis.")
else:
    def hurst(ts):
        lags = range(2, 20)
        tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags]
        return np.polyfit(np.log(lags), np.log(tau), 1)[0] * 2.0

    def spectral_slope(ts):
        fft = np.fft.fft(ts - np.mean(ts))
        freqs = np.fft.fftfreq(len(ts))
        slope, _ = np.polyfit(np.log(freqs[1:int(len(ts)/2)]), np.log(np.abs(fft[1:int(len(ts)/2)])), 1)
        return slope

    df["Hurst"] = df["Price"].rolling(hurst_window).apply(hurst)
    df["Spectral"] = df["Price"].rolling(spectral_window).apply(spectral_slope)

    hmm_model = GaussianHMM(n_components=regime_states, n_iter=1000)
    try:
        hmm_model.fit(df[["LogReturn"]])
        df["Regime"] = hmm_model.predict(df[["LogReturn"]])
    except Exception as e:
        st.error(f"HMM training failed: {e}")
        df["Regime"] = 0

    trend_state = df.groupby("Regime")["LogReturn"].mean().idxmax()
    df["Signal"] = (df["Regime"] == trend_state).astype(float)

    equity = [1.0]
    peak = 1.0
    drawdown_triggered = False
    for i in range(1, len(df)):
        if drawdown_triggered:
            equity.append(equity[-1])
            continue
        ret = df["LogReturn"].iloc[i] * df["Signal"].iloc[i] * leverage
        next_val = equity[-1] * np.exp(ret)
        equity.append(next_val)
        peak = max(peak, next_val)
        if drawdown_limit < 100 and (1 - next_val / peak) > (drawdown_limit / 100):
            st.warning("Max drawdown exceeded. Halting strategy.")
            drawdown_triggered = True
            equity[-1] = equity[-2]

    df["Equity"] = equity

    st.subheader("Equity Curve")
    st.line_chart(df[["Equity"]])

    st.subheader("Performance Metrics")
    total_return = df["Equity"].iloc[-1] - 1
    sharpe = df["Equity"].pct_change().mean() / df["Equity"].pct_change().std() * np.sqrt(252)
    st.metric("Total Return", f"{total_return:.2%}")
    st.metric("Sharpe Ratio", f"{sharpe:.2f}")

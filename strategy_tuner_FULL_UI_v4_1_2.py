
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from hmmlearn.hmm import GaussianHMM
from scipy.signal import welch
import matplotlib.pyplot as plt
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")
st.title("📈 Strategy Tuner v4.1.2 – Stable Release")

ticker = st.sidebar.text_input("Ticker", "SPY")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2010-01-01"))
end_date = st.sidebar.date_input("End Date", datetime.today())

hurst_threshold = st.sidebar.slider("Hurst Threshold", 0.3, 0.9, 0.5)
spectral_threshold = st.sidebar.slider("Spectral Slope Threshold", -4.0, -0.1, -2.0)
leverage_trend = st.sidebar.slider("Leverage (Trend)", 0.0, 5.0, 1.0)
leverage_chop = st.sidebar.slider("Leverage (Chop)", 0.0, 5.0, 0.25)
n_states = st.sidebar.slider("HMM Regimes", 2, 4, 2)

slippage_pct = st.sidebar.slider("Slippage (%)", 0.0, 1.0, 0.1)
commission_pct = st.sidebar.slider("Commission (%)", 0.0, 1.0, 0.05)

@st.cache_data
def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    if 'Adj Close' in df.columns:
        df['Price'] = df['Adj Close']
    elif 'Close' in df.columns:
        df['Price'] = df['Close']
        st.warning("Using 'Close' instead of 'Adj Close'. Results may differ slightly.")
    else:
        st.error("Neither 'Adj Close' nor 'Close' is available in the dataset.")
        return pd.DataFrame()
    df['LogReturn'] = np.log(df['Price'] / df['Price'].shift(1))
    return df.dropna()

def hurst(ts):
    lags = range(2, 20)
    tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags]
    return np.polyfit(np.log(lags), np.log(tau), 1)[0]

def spectral(ts):
    freqs, psd = welch(ts, nperseg=min(256, len(ts)))
    return np.polyfit(np.log(freqs[1:]), np.log(psd[1:]), 1)[0]

df = load_data(ticker, start_date, end_date)

if df.empty:
    st.stop()

try:
    H = hurst(df['LogReturn'].values)
    S = spectral(df['LogReturn'].values)
    df['Hurst'] = H
    df['Spectral'] = S

    X = df[['LogReturn']].dropna()
    if len(X) < n_states:
        st.warning("Not enough data to fit the HMM. Try increasing the date range.")
        st.stop()

    hmm = GaussianHMM(n_components=n_states, n_iter=1000)
    regimes = hmm.fit_predict(X)
    df = df.iloc[-len(regimes):].copy()
    df['Regime'] = regimes

    dominant = df['Regime'].value_counts().idxmax()
    df['Signal'] = np.where(df['Regime'] == dominant, leverage_trend, leverage_chop)

    equity = []
    capital = 1.0
    pos = 0.0
    trade_log = []

    for i in range(1, len(df)):
        price_return = df['LogReturn'].iloc[i]
        signal = df['Signal'].iloc[i]

        if signal != pos:
            capital *= 1 - (slippage_pct + commission_pct)/100
            trade_log.append((df.index[i], pos, signal))
            pos = signal

        capital *= np.exp(pos * price_return)
        equity.append(capital)

    df = df.iloc[1:].copy()
    df['Equity'] = equity

    st.subheader("📈 Equity Curve")
    fig, ax = plt.subplots(figsize=(10, 4))
    df['Equity'].plot(ax=ax, label="Strategy")
    (df['Price'] / df['Price'].iloc[0]).plot(ax=ax, label="Buy & Hold", alpha=0.4)
    ax.set_title("Cumulative Returns")
    ax.legend()
    st.pyplot(fig)

    st.subheader("📊 Performance Metrics")
    total_return = df['Equity'].iloc[-1] - 1
    sharpe = df['Equity'].pct_change().mean() / df['Equity'].pct_change().std() * np.sqrt(252)
    st.metric("Total Return", f"{total_return:.2%}")
    st.metric("Sharpe Ratio", f"{sharpe:.2f}")
    st.metric("Trades Executed", len(trade_log))

    st.subheader("📋 Trade Log")
    trade_df = pd.DataFrame(trade_log, columns=["Date", "From", "To"]).set_index("Date")
    st.dataframe(trade_df.tail(20))

except Exception as e:
    st.error(f"Error during simulation: {e}")

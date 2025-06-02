
# strategy_tuner_FULL_UI_FINAL_ENHANCED_FIXED.py
# Full-featured Streamlit app

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from hmmlearn.hmm import GaussianHMM
import matplotlib.pyplot as plt
import datetime
from io import StringIO
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")
st.title("📈 Strategy Tuner: FULL UI - FINAL ENHANCED VERSION")

# --- Sidebar Inputs ---
st.sidebar.header("🔧 Strategy Configuration")
ticker = st.sidebar.text_input("Ticker Symbol", value="SPY")
start_date = st.sidebar.date_input("Start Date", datetime.date(2015, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date.today())
hurst_threshold = st.sidebar.slider("Hurst Threshold", 0.4, 0.6, 0.5, 0.01)
spectral_threshold = st.sidebar.slider("Spectral Slope Threshold", -1.0, 0.0, -0.5, 0.01)
leverage_trend = st.sidebar.slider("Trend Regime Leverage", 1.0, 5.0, 2.0)
leverage_chop = st.sidebar.slider("Chop Regime Leverage", 0.0, 2.0, 1.0)
show_hmm_states = st.sidebar.checkbox("Show Regime Labels", value=True)
long_only = st.sidebar.checkbox("Long Only Mode", value=False)

# --- Data Fetching ---
@st.cache_data
def fetch_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df = df[["Close"]].rename(columns={"Close": ticker})
    df.index.name = "Date"
    return df

try:
    df = fetch_data(ticker, start_date, end_date)
    df["LogRet"] = np.log(df[ticker] / df[ticker].shift(1))
    df.dropna(inplace=True)
except:
    st.error("Failed to fetch or process price data.")
    st.stop()

# --- Feature Engineering ---
def compute_features(series):
    log_returns = series.pct_change().dropna()
    lags = range(2, 20)
    hurst = np.mean([(np.log(np.std(series.diff(l))) - np.log(np.std(series))) / np.log(l)
                     for l in lags if l < len(series)])
    spectral = np.polyfit(np.log(np.arange(1, len(log_returns) + 1)),
                          np.log(np.abs(np.fft.fft(log_returns))[1:]), 1)[0]
    return hurst, spectral

hurst, spectral = compute_features(df[ticker])
st.markdown(f"**📊 Hurst Exponent:** {hurst:.4f} | **Spectral Slope:** {spectral:.4f}")

# --- HMM Regime Detection ---
if len(df) < 100:
    st.warning("Not enough data to train HMM. Please increase date range.")
    st.stop()

X = df["LogRet"].values.reshape(-1, 1)
model = GaussianHMM(n_components=2, covariance_type="full", n_iter=100)
model.fit(X)
hidden_states = model.predict(X)
df["Regime"] = hidden_states

# Identify which state is "trend" based on mean return
means = model.means_.flatten()
trend_state = np.argmax(means)
df["Signal"] = np.where(df["Regime"] == trend_state, 1, -1 if not long_only else 0)

# Leverage
df["Leverage"] = np.where(df["Regime"] == trend_state, leverage_trend, leverage_chop)
df["StratRet"] = df["Signal"].shift(1) * df["LogRet"] * df["Leverage"]
df["Equity"] = (df["StratRet"] + 1).cumprod()

# --- Plots ---
st.subheader("📈 Equity Curve")
fig, ax = plt.subplots(figsize=(10, 4))
df["Equity"].plot(ax=ax, label="Strategy Equity")
(df[ticker] / df[ticker].iloc[0]).plot(ax=ax, label="Buy & Hold", alpha=0.5)
ax.set_ylabel("Cumulative Return")
ax.legend()
st.pyplot(fig)

# --- Trade Log ---
st.subheader("📜 Trade Log")
df["Trade"] = df["Signal"].diff().fillna(0).astype(int)
trades = df[df["Trade"] != 0].copy()
trades["Action"] = trades["Trade"].map({1: "Long Entry", -1: "Exit" if long_only else "Short Entry"})
trades_display = trades[["Action", ticker, "Regime", "Leverage", "Equity"]]
st.dataframe(trades_display)

# --- Download Log ---
st.download_button(
    label="📥 Download Trade Log",
    data=trades_display.to_csv(index=True),
    file_name=f"{ticker}_strategy_trades.csv",
    mime="text/csv"
)

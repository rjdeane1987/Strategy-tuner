
import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("📈 Strategy Tuner with Regime Detection, Leverage Scaling, and Mean Reversion")

# --- Inputs ---
col1, col2, col3 = st.columns(3)
with col1:
    ticker = st.text_input("Ticker", "SPY")
with col2:
    start_date = st.date_input("Start Date", pd.to_datetime("2015-01-01"))
with col3:
    end_date = st.date_input("End Date", pd.to_datetime("2024-12-31"))

col4, col5, col6 = st.columns(3)
with col4:
    hurst_window = st.slider("Hurst Lookback Window", 20, 250, 90)
with col5:
    spectral_window = st.slider("Spectral Lookback Window", 20, 250, 90)
with col6:
    n_hidden_states = st.selectbox("HMM Regimes", [2, 3])

col7, col8, col9 = st.columns(3)
with col7:
    long_leverage = st.slider("Long Regime Leverage", 1.0, 5.0, 1.5)
with col8:
    short_leverage = st.slider("Short Regime Leverage", 0.5, 3.0, 1.0)
with col9:
    strategy_mode = st.radio("Strategy Type", ["Long-Only", "Long/Short"])

# --- Data Fetch ---
@st.cache_data(ttl=3600)
def get_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df = df[['Close']].dropna()
    df.columns = ['Price']
    df['Returns'] = np.log(df['Price'] / df['Price'].shift(1))
    return df.dropna()

df = get_data(ticker, start_date, end_date)

# --- Feature Calculation ---
def compute_hurst(prices, window):
    if len(prices) < window + 2:
        return pd.Series(np.nan, index=prices.index)
    hurst_vals = []
    for i in range(window, len(prices)):
        ts = prices[i - window:i]
        if np.std(ts) == 0:
            hurst_vals.append(np.nan)
            continue
        lags = range(2, 20)
        tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags]
        m = np.polyfit(np.log(lags), np.log(tau), 1)
        hurst_vals.append(m[0])
    return pd.Series([np.nan] * window + hurst_vals, index=prices.index)

def compute_spectral(prices, window):
    spectral_vals = [np.nan] * window
    for i in range(window, len(prices)):
        segment = prices[i - window:i]
        fft = np.fft.fft(segment - np.mean(segment))
        power = np.abs(fft)**2
        freqs = np.fft.fftfreq(len(segment))
        mask = freqs > 0
        slope = np.polyfit(np.log(freqs[mask]), np.log(power[mask]), 1)[0]
        spectral_vals.append(slope)
    return pd.Series(spectral_vals, index=prices.index)

df["Hurst"] = compute_hurst(df["Price"], hurst_window)
df["Spectral"] = compute_spectral(df["Price"], spectral_window)
df.dropna(inplace=True)

# --- Regime Detection ---
X = df[["Returns", "Hurst", "Spectral"]].dropna()
hmm = GaussianHMM(n_components=n_hidden_states, covariance_type="diag", n_iter=1000, random_state=42)
hmm.fit(X)
df.loc[X.index, "Regime"] = hmm.predict(X)

# --- Strategy Logic ---
def apply_strategy(df, mode, long_lev, short_lev):
    signal = np.zeros(len(df))
    for i in range(len(df)):
        if df["Regime"].iloc[i] == 0:
            signal[i] = long_lev
        else:
            signal[i] = -short_lev if mode == "Long/Short" else 0
    df["Position"] = signal
    df["Strat_Returns"] = df["Returns"] * df["Position"].shift(1)
    df["Equity_Curve"] = (df["Strat_Returns"].fillna(0) + 1).cumprod()
    return df

df = apply_strategy(df, strategy_mode, long_leverage, short_leverage)

# --- Plotting ---
st.subheader("📊 Equity Curve")
fig, ax = plt.subplots(figsize=(12, 4))
df["Equity_Curve"].plot(ax=ax, color="cyan", label="Strategy Equity")
df["Price"].div(df["Price"].iloc[0]).plot(ax=ax, color="gray", alpha=0.5, label="Buy & Hold")
ax.set_ylabel("Growth of $1")
ax.set_title("Equity Curve vs Buy & Hold")
ax.legend()
st.pyplot(fig)

# --- Trade Log ---
st.subheader("🧾 Trade Log")
trade_log = df[df["Position"].diff().abs() > 0][["Position"]]
st.dataframe(trade_log.tail(10))

# --- Stats ---
total_return = df["Equity_Curve"].iloc[-1] - 1
sharpe = df["Strat_Returns"].mean() / df["Strat_Returns"].std() * np.sqrt(252)
st.metric("Total Return", f"{total_return:.2%}")
st.metric("Sharpe Ratio", f"{sharpe:.2f}")

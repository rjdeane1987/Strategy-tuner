
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Manual Strategy Tuner", layout="wide")

st.title("📈 Manual Strategy Tuner (Simplified)")

# Simulate price data
np.random.seed(42)
dates = pd.date_range(start="2013-01-01", end="2024-12-31", freq="D")
returns = np.random.normal(0.0006, 0.014, len(dates))
prices = pd.Series(np.cumprod(1 + returns) * 100, index=dates)

# Sidebar controls
st.sidebar.header("🔧 Strategy Inputs")
hurst_thresh = st.sidebar.slider("Hurst Threshold", 0.45, 0.65, 0.52, 0.01)
slope_thresh = st.sidebar.slider("Spectral Slope Max", -0.5, 0.0, -0.1, 0.01)

# Simulate indicators
hurst = pd.Series(np.random.normal(0.5, 0.05, len(dates)), index=dates).clip(0, 1)
spectral_slope = pd.Series(np.random.normal(-0.2, 0.1, len(dates)), index=dates)

# Signal condition
active = (hurst > hurst_thresh) & (spectral_slope < slope_thresh)

# Apply strategy returns
strategy_returns = pd.Series(returns, index=dates).where(active, 0)
equity_curve = (1 + strategy_returns).cumprod()

# Performance metrics
def compute_metrics(equity):
    rets = equity.pct_change().dropna()
    cagr = (equity.iloc[-1])**(252 / len(equity)) - 1
    vol = rets.std() * np.sqrt(252)
    sharpe = cagr / vol if vol > 0 else 0
    mdd = (equity / equity.cummax() - 1).min()
    return cagr, vol, sharpe, mdd

cagr, vol, sharpe, mdd = compute_metrics(equity_curve)

# Layout
col1, col2 = st.columns(2)
with col1:
    st.subheader("📉 Equity Curve")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(equity_curve.index, equity_curve.values, label="Equity")
    ax.set_title("Equity Curve")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Return")
    ax.grid(True)
    st.pyplot(fig)

with col2:
    st.subheader("📊 Metrics")
    st.metric("CAGR", f"{cagr:.2%}")
    st.metric("Volatility", f"{vol:.2%}")
    st.metric("Sharpe Ratio", f"{sharpe:.2f}")
    st.metric("Max Drawdown", f"{mdd:.2%}")

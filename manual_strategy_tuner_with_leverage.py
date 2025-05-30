
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Manual Strategy Tuner", layout="wide")
st.title("📈 Manual Strategy Tuner with Leverage Scaling")

# Simulate price data
np.random.seed(42)
dates = pd.date_range(start="2013-01-01", end="2024-12-31", freq="D")
returns = np.random.normal(0.0006, 0.014, len(dates))
prices = pd.Series(np.cumprod(1 + returns) * 100, index=dates)

# Sidebar controls
st.sidebar.header("🔧 Strategy Inputs")
use_best = st.sidebar.checkbox("Use Best Config (Auto-Fill)", value=False)

if use_best:
    hurst_thresh = 0.53
    slope_thresh = -0.15
    low_vol = 0.01
    high_vol = 0.018
else:
    hurst_thresh = st.sidebar.slider("Hurst Threshold", 0.45, 0.65, 0.52, 0.01)
    slope_thresh = st.sidebar.slider("Spectral Slope Max", -0.5, 0.0, -0.1, 0.01)
    low_vol = st.sidebar.slider("Low Volatility Threshold", 0.005, 0.02, 0.01, 0.001)
    high_vol = st.sidebar.slider("High Volatility Threshold", 0.01, 0.03, 0.018, 0.001)

# Simulate indicators
hurst = pd.Series(np.random.normal(0.5, 0.05, len(dates)), index=dates).clip(0, 1)
spectral_slope = pd.Series(np.random.normal(-0.2, 0.1, len(dates)), index=dates)
vol = pd.Series(returns, index=dates).rolling(window=20).std().fillna(0.015)

# Signal condition
active = (hurst > hurst_thresh) & (spectral_slope < slope_thresh)

# Leverage scaling logic
leverage = pd.Series(1.0, index=dates)
leverage[vol < low_vol] = 2.0
leverage[vol > high_vol] = 0.5
leverage = leverage.shift(1).fillna(1)

# Apply strategy returns
strategy_returns = pd.Series(returns, index=dates).where(active, 0)
leveraged_returns = strategy_returns * leverage
equity_curve = (1 + leveraged_returns).cumprod()

# Performance metrics
def compute_metrics(equity):
    rets = equity.pct_change().dropna()
    cagr = (equity.iloc[-1])**(252 / len(equity)) - 1
    vol = rets.std() * np.sqrt(252)
    sharpe = cagr / vol if vol > 0 else 0
    mdd = (equity / equity.cummax() - 1).min()
    return cagr, vol, sharpe, mdd

cagr, vol_val, sharpe, mdd = compute_metrics(equity_curve)

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
    st.metric("Volatility", f"{vol_val:.2%}")
    st.metric("Sharpe Ratio", f"{sharpe:.2f}")
    st.metric("Max Drawdown", f"{mdd:.2%}")

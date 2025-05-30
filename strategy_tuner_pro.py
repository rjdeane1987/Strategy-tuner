
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Strategy Tuner Pro", layout="wide")
st.title("📈 Strategy Tuner Pro (w/ Filters, Stops, Optimizer)")

# Simulate data
np.random.seed(42)
dates = pd.date_range(start="2013-01-01", end="2024-12-31", freq="D")
returns = np.random.normal(0.0006, 0.014, len(dates))
prices = pd.Series(np.cumprod(1 + returns) * 100, index=dates)
hurst = pd.Series(np.random.normal(0.5, 0.05, len(dates)), index=dates).clip(0, 1)
spectral_slope = pd.Series(np.random.normal(-0.2, 0.1, len(dates)), index=dates)
vol = pd.Series(returns, index=dates).rolling(20).std().fillna(0.015)

# Sidebar controls
st.sidebar.header("🔧 Strategy Inputs")
use_best = st.sidebar.checkbox("Use Best Config", value=False)

if use_best:
    hurst_thresh = 0.53
    slope_thresh = -0.15
    low_vol = 0.01
    high_vol = 0.018
    exit_hurst = 0.48
    exit_slope = 0.0
else:
    hurst_thresh = st.sidebar.slider("Hurst Threshold", 0.45, 0.65, 0.52, 0.01)
    slope_thresh = st.sidebar.slider("Spectral Slope Max", -0.5, 0.0, -0.15, 0.01)
    low_vol = st.sidebar.slider("Low Volatility Threshold", 0.005, 0.02, 0.01, 0.001)
    high_vol = st.sidebar.slider("High Volatility Threshold", 0.01, 0.03, 0.018, 0.001)
    exit_hurst = st.sidebar.slider("Exit Hurst Threshold", 0.40, 0.55, 0.48, 0.01)
    exit_slope = st.sidebar.slider("Exit Slope Threshold", -0.1, 0.2, 0.0, 0.01)

use_stopout = st.sidebar.checkbox("Enable Drawdown Stop-Out", value=True)
stopout_threshold = st.sidebar.slider("Max Drawdown Threshold", -0.5, -0.1, -0.2, 0.01)

# Signal and leverage logic
active = (hurst > hurst_thresh) & (spectral_slope < slope_thresh)
exit_filter = (hurst < exit_hurst) | (spectral_slope > exit_slope)
signal = active & ~exit_filter

leverage = pd.Series(1.0, index=dates)
leverage[vol < low_vol] = 2.0
leverage[vol > high_vol] = 0.5
leverage = leverage.shift(1).fillna(1)

strategy_returns = pd.Series(returns, index=dates).where(signal, 0)
leveraged_returns = strategy_returns * leverage

# Apply drawdown stop-out
equity = (1 + leveraged_returns).cumprod()
if use_stopout:
    peak = equity.cummax()
    drawdown = (equity / peak) - 1
    equity[drawdown < stopout_threshold] = np.nan
    equity = equity.ffill().fillna(method="bfill")

# Metrics function
def compute_metrics(equity):
    rets = equity.pct_change().dropna()
    cagr = (equity.iloc[-1])**(252 / len(equity)) - 1
    vol = rets.std() * np.sqrt(252)
    sharpe = cagr / vol if vol > 0 else 0
    mdd = (equity / equity.cummax() - 1).min()
    return cagr, vol, sharpe, mdd

cagr, vol_val, sharpe, mdd = compute_metrics(equity)

# Sharpe optimizer
st.sidebar.markdown("---")
if st.sidebar.button("🔍 Optimize Sharpe (Scan Grid)"):
    best_sharpe, best_h, best_s = 0, 0, 0
    for h in np.arange(0.50, 0.56, 0.01):
        for s in np.arange(-0.2, -0.09, 0.01):
            sig = (hurst > h) & (spectral_slope < s)
            filt = (hurst < exit_hurst) | (spectral_slope > exit_slope)
            combined = sig & ~filt
            ret = pd.Series(returns, index=dates).where(combined, 0) * leverage
            eq = (1 + ret).cumprod()
            if use_stopout:
                dd = (eq / eq.cummax()) - 1
                eq[dd < stopout_threshold] = np.nan
                eq = eq.ffill().fillna(method="bfill")
            _, _, curr_sharpe, _ = compute_metrics(eq)
            if curr_sharpe > best_sharpe:
                best_sharpe, best_h, best_s = curr_sharpe, h, s
    st.sidebar.success(f"Best Sharpe: {best_sharpe:.2f} at Hurst={best_h:.2f}, Slope={best_s:.2f}")

# Display
col1, col2 = st.columns(2)
with col1:
    st.subheader("📉 Equity Curve")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(equity.index, equity.values, label="Equity")
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

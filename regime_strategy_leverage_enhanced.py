import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("Regime-Switching Strategy with Leverage Scaling")

# Sidebar inputs
st.sidebar.header("Strategy Configuration")
asset = st.sidebar.selectbox("Asset", ["BTC-USD", "QQQ", "SPY"])
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2013-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-31"))

trend_leverage = st.sidebar.slider("Trend Regime Leverage", 0.0, 3.0, 1.0, 0.1)
chop_leverage = st.sidebar.slider("Chop Regime Leverage", 0.0, 3.0, 1.0, 0.1)
vol_targeting = st.sidebar.checkbox("Enable Volatility Targeting", value=False)
target_vol = st.sidebar.slider("Target Volatility", 0.05, 0.5, 0.15, 0.01)

# Download data
@st.cache
def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df = df["Adj Close"].to_frame(name="price")
    df["returns"] = df["price"].pct_change()
    return df.dropna()

data = load_data(asset, start_date, end_date)

# Simulate regime logic (placeholder logic)
np.random.seed(42)
hurst = pd.Series(np.random.normal(0.5, 0.05, len(data)), index=data.index).clip(0, 1)
spectral = pd.Series(np.random.normal(-0.2, 0.1, len(data)), index=data.index)

data["regime"] = "neutral"
data.loc[(hurst > 0.52) & (spectral < -0.1), "regime"] = "trend"
data.loc[(hurst < 0.48) | (spectral > 0.0), "regime"] = "chop"

ema = data["price"].ewm(span=20).mean()
std = data["price"].rolling(20).std().bfill()
zscore = (data["price"] - ema) / std

capital = 1.0
equity = []
position = 0
entry_price = 0
log = []

for i in range(1, len(data)):
    row = data.iloc[i]
    prev_row = data.iloc[i - 1]
    regime = row["regime"]
    leverage = 1.0
    if regime == "trend":
        leverage = trend_leverage
        capital *= 1 + leverage * row["returns"]
        log.append((row.name, "trend", leverage, capital))
    elif regime == "chop":
        leverage = chop_leverage
        if zscore.iloc[i - 1] < -1.5:
            position = 1
            entry_price = prev_row["price"]
        elif zscore.iloc[i - 1] > 1.5:
            position = -1
            entry_price = prev_row["price"]
        if position != 0:
            ret = (row["price"] - entry_price) / entry_price
            capital *= 1 + leverage * ret * position
            log.append((row.name, "chop", leverage, capital))
            position = 0
    equity.append(capital)

data = data.iloc[1:]
data["equity"] = equity

# Plot
fig, ax = plt.subplots(figsize=(12, 5))
data["equity"].plot(ax=ax, label="Strategy")
data["price"].plot(ax=ax, label="Price", secondary_y=True, alpha=0.4)
for regime_type in ["trend", "chop"]:
    mask = data["regime"] == regime_type
    ax.fill_between(data.index, 0, data["equity"], where=mask, alpha=0.2, label=f"{regime_type} regime")

ax.set_title("Equity Curve with Regime Overlays")
ax.legend()
st.pyplot(fig)

# Stats
rets = data["equity"].pct_change().dropna()
cagr = (data["equity"].iloc[-1])**(252 / len(data)) - 1
vol = rets.std() * np.sqrt(252)
sharpe = cagr / vol if vol > 0 else 0
mdd = (data["equity"] / data["equity"].cummax() - 1).min()

st.subheader("Performance Metrics")
st.write(f"CAGR: {cagr:.2%}")
st.write(f"Volatility: {vol:.2%}")
st.write(f"Sharpe Ratio: {sharpe:.2f}")
st.write(f"Max Drawdown: {mdd:.2%}")

# Trade log
log_df = pd.DataFrame(log, columns=["Date", "Regime", "Leverage", "Equity"])
st.subheader("Trade Log")
st.dataframe(log_df.set_index("Date"))
st.download_button("Download Trade Log CSV", log_df.to_csv().encode(), "trade_log.csv", "text/csv")

import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# -------------------- Data Loader --------------------
def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df = df["Close"].to_frame(name="price")
    df["returns"] = df["price"].pct_change()
    return df.dropna()

# -------------------- Regime Detector --------------------
def detect_regime(data, window, upper, lower):
    zscore = (data['returns'] - data['returns'].rolling(window).mean()) / data['returns'].rolling(window).std()
    regime = np.where(zscore > upper, "trend", np.where(zscore < lower, "trend", "chop"))
    data["regime"] = regime
    return data.dropna()

# -------------------- Trade Log Generator --------------------
def generate_trade_log(data):
    trade_log = []
    last_regime = None
    entry_date = None
    entry_price = None

    for date, row in data.iterrows():
        current_regime = row['regime']
        if current_regime != last_regime:
            if last_regime is not None:
                trade_log.append({
                    "Start Date": entry_date,
                    "End Date": date,
                    "Regime": last_regime,
                    "Entry Price": entry_price,
                    "Exit Price": row['price'],
                    "Return": (row['price'] / entry_price) - 1 if entry_price else np.nan
                })
            entry_date = date
            entry_price = row['price']
            last_regime = current_regime

    return pd.DataFrame(trade_log)

# -------------------- Streamlit UI --------------------
st.title("Regime-Switching Strategy with Z-Score Detection")

asset = st.text_input("Asset Symbol", "BTC-USD")
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2024-12-31"))

trend_leverage = st.slider("Trend Regime Leverage", 0.0, 5.0, 2.0, 0.1)
chop_leverage = st.slider("Chop Regime Leverage", 0.0, 5.0, 0.5, 0.1)

zscore_window = st.slider("Z-Score Lookback Window", 5, 60, 20, 1)
upper_threshold = st.slider("Z-Score Upper Threshold", 0.0, 2.0, 0.5, 0.1)
lower_threshold = st.slider("Z-Score Lower Threshold", -2.0, 0.0, -0.5, 0.1)

if start_date >= end_date:
    st.error("Start date must be before end date.")
    st.stop()

data = load_data(asset, start_date, end_date)
data = detect_regime(data, zscore_window, upper_threshold, lower_threshold)

# Apply leverage
leverage_map = {'trend': trend_leverage, 'chop': chop_leverage}
data["leverage"] = data["regime"].map(leverage_map)
data["strategy_returns"] = data["returns"] * data["leverage"]
data["cumulative_strategy"] = (1 + data["strategy_returns"]).cumprod()
data["cumulative_asset"] = (1 + data["returns"]).cumprod()

# -------------------- Plotting --------------------
st.subheader("Cumulative Returns")
fig, ax = plt.subplots()
ax.plot(data.index, data["cumulative_strategy"], label="Strategy", linewidth=2)
ax.plot(data.index, data["cumulative_asset"], label=asset, linewidth=1.5, linestyle="--")

# Regime overlay
regime_colors = {"trend": "green", "chop": "red"}
for regime, color in regime_colors.items():
    mask = data["regime"] == regime
    ax.fill_between(data.index, 0, 1, where=mask, transform=ax.get_xaxis_transform(),
                    alpha=0.05, color=color, label=f"{regime} zone")

ax.legend()
ax.set_ylabel("Cumulative Return")
st.pyplot(fig)

# -------------------- Summary Stats --------------------
st.subheader("Performance Metrics")
total_return = data["cumulative_strategy"].iloc[-1] - 1
volatility = data["strategy_returns"].std() * np.sqrt(252)
sharpe = data["strategy_returns"].mean() / data["strategy_returns"].std() * np.sqrt(252)

st.metric("Total Return", f"{total_return:.2%}")
st.metric("Annualized Volatility", f"{volatility:.2%}")
st.metric("Sharpe Ratio", f"{sharpe:.2f}")

# -------------------- Trade Log --------------------
st.subheader("Trade Log")
log_df = generate_trade_log(data)
st.dataframe(log_df)

# -------------------- Downloads --------------------
csv_strategy = data.to_csv().encode("utf-8")
csv_log = log_df.to_csv().encode("utf-8")

st.download_button("Download Strategy Data CSV", csv_strategy, "strategy_output.csv", "text/csv")
st.download_button("Download Trade Log CSV", csv_log, "trade_log.csv", "text/csv")

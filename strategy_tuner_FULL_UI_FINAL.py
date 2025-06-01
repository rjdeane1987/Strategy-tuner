
import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM
from scipy.signal import welch
from scipy.stats import linregress
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📈 Strategy Tuner Pro – Final Version with Hurst, Spectral, HMM, Equity Curve & Trade Log")

# Sidebar Controls
st.sidebar.header("📊 Configuration")
ticker = st.sidebar.selectbox("Asset", ["SPY", "BTC-USD", "QQQ", "NQ=F"])
start = st.sidebar.date_input("Start Date", pd.to_datetime("2010-01-01"))
end = st.sidebar.date_input("End Date", pd.to_datetime("2025-06-01"))

st.sidebar.subheader("🧠 Regime Filters")
hurst_min = st.sidebar.slider("Min Hurst", -1.0, 1.0, 0.0, 0.01)
hurst_max = st.sidebar.slider("Max Hurst", -1.0, 1.0, 0.8, 0.01)
spectral_min = st.sidebar.slider("Min Spectral Slope", -10.0, 0.0, -6.0, 0.1)
spectral_max = st.sidebar.slider("Max Spectral Slope", -10.0, 0.0, -0.5, 0.1)

st.sidebar.subheader("⚙️ Regime-Specific Leverage")
trend_lev = st.sidebar.slider("Trend Leverage", 0.0, 5.0, 1.0, 0.1)
chop_lev = st.sidebar.slider("Chop Leverage", 0.0, 5.0, 1.0, 0.1)

st.sidebar.subheader("🎯 Volatility Targeting")
vol_targeting = st.sidebar.checkbox("Enable Vol Targeting", value=False)
target_vol = st.sidebar.slider("Target Volatility", 0.05, 0.5, 0.15, 0.01)

@st.cache_data
def fetch_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end, auto_adjust=False)
    df = df[['Adj Close']].rename(columns={'Adj Close': 'price'})
    df["returns"] = np.log(df["price"] / df["price"].shift(1))
    return df.dropna()

def compute_hurst(ts):
    lags = range(2, 20)
    try:
        tau = [np.std(ts.diff(lag).dropna()) for lag in lags if lag < len(ts)]
        if any([t <= 0 for t in tau]):
            return np.nan
        log_lags = np.log(lags[:len(tau)])
        log_tau = np.log(tau)
        slope, _ = np.polyfit(log_lags, log_tau, 1)
        return slope
    except:
        return np.nan

def compute_spectral_slope(ts):
    ts = ts.dropna()
    if len(ts) < 8:
        return np.nan
    fft_vals = np.abs(np.fft.fft(ts))**2
    freqs = np.fft.fftfreq(len(ts))
    valid = (freqs > 0) & (fft_vals > 0)
    if valid.sum() < 2:
        return np.nan
    slope, _ = np.polyfit(np.log(freqs[valid]), np.log(fft_vals[valid]), 1)
    return slope

df = fetch_data(ticker, start, end)
df["hurst"] = df["returns"].rolling(50).apply(compute_hurst, raw=False).bfill()
df["spectral"] = df["returns"].rolling(50).apply(compute_spectral_slope, raw=False).bfill()
df = df.dropna()

obs = df[["hurst", "spectral"]].dropna().values
st.write(f"✅ Rows available for HMM training: {len(obs)}")
if len(obs) < 10:
    st.warning("⚠️ Not enough data to fit the HMM.")
    st.stop()

model = GaussianHMM(n_components=2, covariance_type="full", n_iter=1000).fit(obs)
df.loc[df.index[-len(obs):], "regime"] = model.predict(obs)

trend_label = df.groupby("regime")["returns"].mean().idxmax()
df["regime_label"] = df["regime"].apply(lambda x: "trend" if x == trend_label else "chop")

df = df[(df["hurst"] >= hurst_min) & (df["hurst"] <= hurst_max)]
df = df[(df["spectral"] >= spectral_min) & (df["spectral"] <= spectral_max)]

zscore = (df["price"] - df["price"].rolling(20).mean()) / df["price"].rolling(20).std()
df["zscore"] = zscore

capital = 1.0
equity = []
position = 0
entry_price = 0
log = []

rolling_vol = df["returns"].rolling(20).std().bfill()

for i in range(1, len(df)):
    row = df.iloc[i]
    prev = df.iloc[i - 1]
    lev = 1.0
    if row["regime_label"] == "trend":
        lev = trend_lev
        if vol_targeting and rolling_vol.iloc[i] > 0:
            lev *= target_vol / rolling_vol.iloc[i]
        capital *= 1 + lev * row["returns"]
        log.append((row.name, "trend", lev, capital))
    elif row["regime_label"] == "chop":
        lev = chop_lev
        if vol_targeting and rolling_vol.iloc[i] > 0:
            lev *= target_vol / rolling_vol.iloc[i]
        if df["zscore"].iloc[i - 1] < -1.5:
            position = 1
            entry_price = prev["price"]
        elif df["zscore"].iloc[i - 1] > 1.5:
            position = -1
            entry_price = prev["price"]
        if position != 0:
            pnl = (row["price"] - entry_price) / entry_price
            capital *= 1 + lev * pnl * position
            log.append((row.name, "chop", lev * position, capital))
            position = 0
    equity.append(capital)

df = df.iloc[1:]
df["equity"] = equity

fig, ax = plt.subplots(figsize=(12, 5))
df["equity"].plot(ax=ax, label="Strategy")
df["price"].plot(ax=ax, secondary_y=True, label="Price", alpha=0.3)
for label in ["trend", "chop"]:
    ax.fill_between(df.index, 0, df["equity"], where=df["regime_label"] == label, alpha=0.15, label=f"{label} regime")
ax.set_title("Equity Curve with Regimes")
ax.legend()
st.pyplot(fig)

rets = pd.Series(df["equity"]).pct_change().dropna()
cagr = (df["equity"].iloc[-1])**(252 / len(df)) - 1
vol = rets.std() * np.sqrt(252)
sharpe = cagr / vol if vol > 0 else 0
mdd = (df["equity"] / df["equity"].cummax() - 1).min()

st.subheader("📊 Performance Summary")
st.write(f"**CAGR:** {cagr:.2%}")
st.write(f"**Volatility:** {vol:.2%}")
st.write(f"**Sharpe Ratio:** {sharpe:.2f}")
st.write(f"**Max Drawdown:** {mdd:.2%}")

log_df = pd.DataFrame(log, columns=["Date", "Regime", "Leverage", "Equity"])
st.subheader("📋 Trade Log")
st.dataframe(log_df.set_index("Date"))
st.download_button("Download Trade Log", log_df.to_csv(index=False).encode(), "trade_log.csv", "text/csv")

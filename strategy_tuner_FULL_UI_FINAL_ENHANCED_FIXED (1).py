
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM
from scipy.signal import welch
from numpy.fft import rfft
from io import BytesIO

st.set_page_config(page_title="Strategy Tuner", layout="wide")
st.title("📈 Strategy Tuner: Full Logic Restored")

# Sidebar Inputs
ticker = st.sidebar.text_input("Ticker", value="SPY")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2010-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))

hurst_threshold = st.sidebar.slider("Hurst Threshold", 0.3, 0.8, 0.5, 0.01)
spectral_slope_threshold = st.sidebar.slider("Spectral Slope Threshold", -5.0, 0.0, -2.0, 0.1)
leverage_trend = st.sidebar.slider("Leverage (Trend)", 0.5, 5.0, 2.0, 0.1)
leverage_chop = st.sidebar.slider("Leverage (Chop)", 0.0, 2.0, 0.5, 0.1)
n_states = st.sidebar.slider("HMM Regimes", 2, 4, 2)

# Load data
@st.cache_data
def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df = df[['Close']].rename(columns={'Close': 'price'})
    df.dropna(inplace=True)
    df['log_return'] = np.log(df['price'] / df['price'].shift(1))
    df.dropna(inplace=True)
    return df

df = load_data(ticker, start_date, end_date)

# Hurst Exponent
def hurst(ts, max_lag=100):
    lags = range(2, max_lag)
    tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags]
    return np.polyfit(np.log(lags), np.log(tau), 1)[0]

# Spectral Slope
def spectral_slope(ts):
    freqs, psd = welch(ts, nperseg=min(256, len(ts)))
    log_freqs = np.log(freqs[1:])
    log_psd = np.log(psd[1:])
    slope, _ = np.polyfit(log_freqs, log_psd, 1)
    return slope

# HMM Regime Assignment
def fit_hmm(data, n_components):
    model = GaussianHMM(n_components=n_components, covariance_type="diag", n_iter=1000)
    model.fit(data.reshape(-1, 1))
    hidden_states = model.predict(data.reshape(-1, 1))
    return hidden_states

# Analysis
try:
    h = hurst(df['log_return'].values)
    s = spectral_slope(df['log_return'].values)
    df['regime'] = fit_hmm(df['log_return'].values, n_states)

    if h > hurst_threshold and s < spectral_slope_threshold:
        st.success(f"✅ Conditions favorable (H={h:.2f}, Spectral Slope={s:.2f})")
    else:
        st.warning(f"⚠️ Market not ideal (H={h:.2f}, Spectral Slope={s:.2f})")

    df['signal'] = 0
    dominant = df['regime'].value_counts().idxmax()
    df['signal'] = df['regime'].apply(lambda x: leverage_trend if x == dominant else leverage_chop)
    df['strategy_return'] = df['log_return'] * df['signal']
    df['equity_curve'] = df['strategy_return'].cumsum().apply(np.exp)

    st.subheader("📊 Equity Curve")
    fig, ax = plt.subplots(figsize=(10, 4))
    df['equity_curve'].plot(ax=ax, label="Strategy")
    df['price'].pct_change().cumsum().apply(np.exp).plot(ax=ax, label="Buy & Hold")
    ax.legend()
    ax.set_title("Cumulative Returns")
    st.pyplot(fig)

    st.subheader("📈 Performance")
    total_return = df['equity_curve'].iloc[-1] - 1
    sharpe = df['strategy_return'].mean() / df['strategy_return'].std() * np.sqrt(252)
    st.markdown(f"- **Total Return**: {total_return:.2%}")
    st.markdown(f"- **Sharpe Ratio**: {sharpe:.2f}")

    # Download button
    csv = df.to_csv().encode()
    st.download_button("📥 Download Strategy Data", csv, "strategy_data.csv")

except Exception as e:
    st.error(f"❌ Error: {e}")


import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM
from scipy.signal import welch

st.set_page_config(layout="wide")
st.title("📈 Strategy Tuner Pro – v4 FIXED (Slippage + Commissions)")

# Sidebar Controls
ticker = st.sidebar.text_input("Ticker", "SPY")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2010-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2025-06-01"))
hurst_thresh = st.sidebar.slider("Hurst Threshold", 0.3, 0.8, 0.5, 0.01)
spectral_thresh = st.sidebar.slider("Spectral Slope Threshold", -5.0, 0.0, -2.0, 0.1)
leverage_trend = st.sidebar.slider("Leverage (Trend)", 0.5, 5.0, 2.0, 0.1)
leverage_chop = st.sidebar.slider("Leverage (Chop)", 0.0, 2.0, 0.5, 0.1)
n_states = st.sidebar.slider("HMM Regimes", 2, 4, 2)

# Slippage & Commission Settings
st.sidebar.subheader("⚙️ Execution Assumptions")
enable_costs = st.sidebar.checkbox("Enable Slippage + Commissions", value=True)
slippage_pct = st.sidebar.slider("Slippage per Side (%)", 0.0, 0.5, 0.1, 0.01) / 100
commission_pct = st.sidebar.slider("Commission (%)", 0.0, 0.5, 0.05, 0.01) / 100

@st.cache_data
def get_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df = df[['Close']].rename(columns={'Close': 'price'})
    df['log_return'] = np.log(df['price'] / df['price'].shift(1))
    return df.dropna()

df = get_data(ticker, start_date, end_date)

def hurst(ts):
    lags = range(2, 20)
    tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags]
    return np.polyfit(np.log(lags), np.log(tau), 1)[0]

def spectral(ts):
    freqs, psd = welch(ts, nperseg=min(256, len(ts)))
    return np.polyfit(np.log(freqs[1:]), np.log(psd[1:]), 1)[0]

try:
    H = hurst(df['log_return'].values)
    S = spectral(df['log_return'].values)
    df['regime'] = GaussianHMM(n_components=n_states, n_iter=1000).fit(df[['log_return']]).predict(df[['log_return']])
    dominant = df['regime'].value_counts().idxmax()
    df['signal'] = np.where(df['regime'] == dominant, leverage_trend, leverage_chop)

    trade_log = []
    capital = 1.0
    equity_curve = []
    position = 0

    equity_dates = []

    for i in range(1, len(df)):
        prev_price = df['price'].iloc[i-1]
        curr_price = df['price'].iloc[i]
        signal = df['signal'].iloc[i]
        ret = np.log(curr_price / prev_price)

        if signal != position:
            if enable_costs:
                ret -= (slippage_pct + commission_pct)
            trade_log.append((df.index[i], position, signal))
            position = signal

        capital *= np.exp(position * ret)
        equity_curve.append(capital)
        equity_dates.append(df.index[i])

    equity_df = pd.DataFrame({'Equity': equity_curve}, index=equity_dates)
    df = df.loc[equity_dates].copy()
    df['Equity'] = equity_df['Equity']
    df['Signal'] = df['signal']

    st.subheader("📈 Equity Curve")
    fig, ax = plt.subplots(figsize=(10, 4))
    df['Equity'].plot(ax=ax, label="Strategy")
    (df['price'] / df['price'].iloc[0]).plot(ax=ax, label="Buy & Hold", alpha=0.4)
    ax.set_title("Cumulative Returns")
    ax.legend()
    st.pyplot(fig)

    st.subheader("📊 Metrics")
    total_return = df['Equity'].iloc[-1] - 1
    sharpe = df['Equity'].pct_change().mean() / df['Equity'].pct_change().std() * np.sqrt(252)
    st.metric("Total Return", f"{total_return:.2%}")
    st.metric("Sharpe Ratio", f"{sharpe:.2f}")
    st.metric("Trades Executed", len(trade_log))

    st.subheader("📋 Trade Log")
    trade_df = pd.DataFrame(trade_log, columns=["Date", "From", "To"]).set_index("Date")
    st.dataframe(trade_df.tail(20))
    st.download_button("📥 Download Trade Log", trade_df.to_csv().encode(), "trade_log.csv")

except Exception as e:
    st.error(f"Error during simulation: {e}")

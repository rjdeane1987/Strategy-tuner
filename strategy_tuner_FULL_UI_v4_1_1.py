
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from hmmlearn.hmm import GaussianHMM
from datetime import datetime
import matplotlib.pyplot as plt

st.set_page_config(page_title="Strategy Tuner v4.1.1", layout="wide")

# Title
st.title("📈 Strategy Tuner v4.1.1")
st.markdown("Enhanced HMM strategy with error handling and full UI")

# Sidebar
ticker = st.sidebar.text_input("Ticker Symbol", value="SPY")
start_date = st.sidebar.date_input("Start Date", datetime(2010, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.today())

hurst_threshold = st.sidebar.slider("Hurst Exponent Threshold", 0.1, 1.0, 0.5, 0.01)
spectral_threshold = st.sidebar.slider("Spectral Slope Threshold", -5.0, 0.0, -2.0, 0.1)

n_hidden_states = st.sidebar.slider("HMM Hidden States", 2, 5, 3)
regime_leverage = {
    0: st.sidebar.slider("Leverage Regime 0", 0.0, 3.0, 1.0),
    1: st.sidebar.slider("Leverage Regime 1", 0.0, 3.0, 1.5),
    2: st.sidebar.slider("Leverage Regime 2", 0.0, 3.0, 2.0)
}

@st.cache_data
def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df['LogReturn'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))
    return df.dropna()

# Load data
try:
    df = load_data(ticker, start_date, end_date)
    if df.empty:
        st.error("The dataset is empty. Try adjusting the date range or ticker.")
    else:
        model_input = df[['LogReturn']].dropna().values
        if model_input.shape[0] < n_hidden_states:
            st.warning("Not enough data points to train the HMM. Please increase your date range.")
        else:
            hmm = GaussianHMM(n_components=n_hidden_states, covariance_type="diag", n_iter=1000)
            hmm.fit(model_input)
            hidden_states = hmm.predict(model_input)
            df['Regime'] = np.nan
            df.loc[df.index[-len(hidden_states):], 'Regime'] = hidden_states

            returns = df['LogReturn'].copy()
            leverage_series = df['Regime'].map(regime_leverage).fillna(1.0)
            strategy_returns = returns * leverage_series.shift(1).fillna(1.0)
            cumulative = (strategy_returns + 1).cumprod()

            fig, ax = plt.subplots()
            ax.plot(df.index, cumulative, label="Strategy", color="orange")
            ax.set_title("Cumulative Returns with Regime-Based Leverage")
            ax.legend()
            st.pyplot(fig)
except Exception as e:
    st.error(f"Error during simulation: {e}")

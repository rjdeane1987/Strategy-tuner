
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from hmmlearn.hmm import GaussianHMM
import matplotlib.pyplot as plt

# Utility functions
def compute_hurst(ts):
    try:
        lags = range(2, 100)
        tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags]
        poly = np.polyfit(np.log(lags), np.log(tau), 1)
        return poly[0]
    except Exception:
        return np.nan

def compute_spectral_slope(ts):
    try:
        ts = ts - np.mean(ts)
        freqs = np.fft.fftfreq(len(ts))
        fft_vals = np.abs(np.fft.fft(ts))**2
        pos_freqs = freqs[freqs > 0]
        pos_fft_vals = fft_vals[freqs > 0]
        slope = np.polyfit(np.log(pos_freqs), np.log(pos_fft_vals), 1)[0]
        return slope
    except Exception:
        return np.nan

# Streamlit UI
st.title("Strategy Tuner - FULL UI FINAL FIXED")

ticker = st.text_input("Enter Ticker Symbol", "SPY")
start_date = st.date_input("Start Date", pd.to_datetime("2010-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2024-12-31"))

if st.button("Run Strategy"):
    df = yf.download(ticker, start=start_date, end=end_date)
    df = df[['Close']].dropna()
    df['Hurst'] = df['Close'].rolling(window=100).apply(compute_hurst)
    df['Spectral'] = df['Close'].rolling(window=100).apply(compute_spectral_slope)
    df.dropna(inplace=True)

    if len(df) < 200:
        st.error("Not enough data to train HMM.")
    else:
        model = GaussianHMM(n_components=2, covariance_type="diag", n_iter=1000)
        model.fit(np.column_stack([df["Hurst"], df["Spectral"]]))
        hidden_states = model.predict(np.column_stack([df["Hurst"], df["Spectral"]]))
        df["regime_label"] = hidden_states
        df["regime_label"] = df["regime_label"].map({0: "trend", 1: "chop"})

        capital = 1.0
        position = 0
        equity_curve = []

        for i in range(len(df)):
            row = df.iloc[i]
            if isinstance(row["regime_label"], str) and row["regime_label"] == "trend":
                if position == 0:
                    position = capital / row["Close"]
                    capital = 0
            elif position != 0:
                capital = position * row["Close"]
                position = 0
            equity_curve.append(capital if capital != 0 else position * row["Close"])

        df["Equity"] = equity_curve

        st.line_chart(df[["Close", "Equity"]])
        st.write("Final Capital:", round(equity_curve[-1], 2))


# DEBUG VERSION OF STRATEGY TUNER

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from hmmlearn.hmm import GaussianHMM
import matplotlib.pyplot as plt
import datetime

def compute_hurst(ts):
    lags = range(2, 20)
    tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags if lag < len(ts)]
    if any(np.array(tau) <= 0):
        return np.nan
    poly = np.polyfit(np.log(lags[:len(tau)]), np.log(tau), 1)
    return poly[0]

def compute_spectral_slope(ts):
    if len(ts.dropna()) < 4:
        return np.nan
    freqs = np.fft.fftfreq(len(ts))
    fft_vals = np.abs(np.fft.fft(ts))**2
    valid = freqs > 0
    slope, _ = np.polyfit(np.log(freqs[valid]), np.log(fft_vals[valid]), 1)
    return slope

st.title("🔬 Strategy Tuner Debug - Hurst & Spectral")

ticker = st.sidebar.text_input("Ticker", "SPY")
start_date = st.sidebar.date_input("Start Date", datetime.date(2010, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date.today())

data = yf.download(ticker, start=start_date, end=end_date)
df = data.copy()
df["returns"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))

df["hurst"] = df["returns"].rolling(50).apply(compute_hurst, raw=False).bfill()
df["spectral"] = df["returns"].rolling(50).apply(compute_spectral_slope, raw=False).bfill()

# Debug outputs
st.subheader("🔍 Debug Preview")
st.write("📉 Hurst (head):", df["hurst"].dropna().head())
st.write("📊 Spectral (head):", df["spectral"].dropna().head())
st.write("✅ Rows available for HMM training:", df[["hurst", "spectral"]].dropna().shape[0])

# Optionally show line chart of the price
st.line_chart(df["Adj Close"])

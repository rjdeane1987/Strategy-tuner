
# DEBUG VERSION OF STRATEGY TUNER - FIXED SPECTRAL SLOPE AND YFINANCE DOWNLOAD

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

st.title("🔬 Strategy Tuner Debug - Hurst & Spectral (Fixed + yfinance patch)")

ticker = st.sidebar.text_input("Ticker", "SPY")
start_date = st.sidebar.date_input("Start Date", datetime.date(2010, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date.today())

# Force adjusted close column to appear
data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)

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

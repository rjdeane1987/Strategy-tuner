
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from hmmlearn.hmm import GaussianHMM
import matplotlib.pyplot as plt
import datetime

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

st.title("🔬 Strategy Tuner Debug - FINAL Hurst & Spectral Patch")

ticker = st.sidebar.text_input("Ticker", "SPY")
start_date = st.sidebar.date_input("Start Date", datetime.date(2010, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date.today())

data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
df = data.copy()
df["returns"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))

df["hurst"] = df["returns"].rolling(50).apply(compute_hurst, raw=False).bfill()
df["spectral"] = df["returns"].rolling(50).apply(compute_spectral_slope, raw=False).bfill()

st.subheader("🔍 Debug Preview")
st.write("📉 Hurst (head):", df["hurst"].dropna().head())
st.write("📊 Spectral (head):", df["spectral"].dropna().head())
st.write("✅ Rows available for HMM training:", df[["hurst", "spectral"]].dropna().shape[0])

st.line_chart(df["Adj Close"])

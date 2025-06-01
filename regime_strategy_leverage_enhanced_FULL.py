import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st

def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    if isinstance(df.columns, pd.MultiIndex):
        df = df['Close']
    else:
        df = df['Close']
    df = df.to_frame(name='price')
    df['returns'] = df['price'].pct_change()
    return df.dropna()

# You can continue your strategy logic here below...


import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import scipy.stats
import scipy.signal
from datetime import datetime
from typing import Dict, Tuple, List
from hmmlearn import hmm
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class MarketAnalyzer:
    """
    Core analysis engine - no bullshit, just pure market intelligence
    """
    def __init__(self):
        self.scaler = StandardScaler()
        
    @staticmethod
    def sma(data: pd.Series, period: int) -> pd.Series:
        return data.rolling(window=period).mean()
    
    @staticmethod
    def ema(data: pd.Series, period: int) -> pd.Series:
        return data.ewm(span=period, adjust=False).mean()
    
    @staticmethod
    def rsi(data: pd.Series, period: int = 14) -> pd.Series:
        delta = data.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def calculate_hurst(self, ts: pd.Series, lags: range) -> float:
        """
        Because markets aren't random, no matter what your professor told you
        """
        tau = [np.sqrt(np.std(np.subtract(ts[lag:], ts[:-lag]))) for lag in lags]
        reg = np.polyfit(np.log(lags), np.log(tau), 1)
        return reg[0]

    def detect_regimes(self, data: pd.DataFrame, n_regimes: int, history: int) -> np.ndarray:
        """
        Market regimes matter more than your technical indicators
        """
        features = np.column_stack([
            data['Close'].pct_change().fillna(0),
            data['Volume'].pct_change().fillna(0),
            data['High'].div(data['Low']).pct_change().fillna(0)
        ])
        
        features = self.scaler.fit_transform(features)
        
        model = hmm.GaussianHMM(
            n_components=n_regimes,
            covariance_type="full",
            n_iter=100
        )
        
        model.fit(features[-history:])
        regimes = model.predict(features)
        
        return regimes

    def spectral_analysis(self, data: pd.Series, window: int) -> float:
        """
        Find the dominant cycle because markets are cyclical
        """
        f, pxx = scipy.signal.periodogram(data)
        return f[np.argmax(pxx)]

class StrategyExecutor:
    def __init__(self):
        self.analyzer = MarketAnalyzer()
        
    def calculate_all_metrics(self, data: pd.DataFrame, params: Dict) -> Dict:
        """
        Calculate every metric that matters - no fluff
        """
        # Base calculations
        data['Returns'] = data['Close'].pct_change()
        data['SMA20'] = self.analyzer.sma(data['Close'], 20)
        data['SMA50'] = self.analyzer.sma(data['Close'], 50)
        data['RSI'] = self.analyzer.rsi(data['Close'])
        
        # Advanced analysis
        regimes = self.analyzer.detect_regimes(
            data, 
            params['n_regimes'], 
            params['hmm_history']
        )
        
        hurst = self.analyzer.calculate_hurst(
            data['Close'], 
            range(2, params['hurst_window'])
        )
        
        dominant_cycle = self.analyzer.spectral_analysis(
            data['Close'], 
            params['spectral_window']
        )

        # Strategy signals
        data['Position'] = np.where(
            (data['SMA20'] > data['SMA50']) & 
            (data['RSI'] < 70) & 
            (regimes == regimes[-1]),
            1, -1
        )
def calculate_performance_metrics(self, data: pd.DataFrame, params: Dict) -> Dict:
        """
        Calculate every goddamn metric that matters
        """
        # Position sizing based on regime and risk
        position_size = params['position_size'] / 100
        risk_multiplier = np.where(data['RSI'] > 70, 0.5,
                                 np.where(data['RSI'] < 30, 1.5, 1.0))
        
        # Returns calculations
        data['Strategy_Returns'] = data['Returns'] * data['Position'].shift(1) * position_size * risk_multiplier
        data['Strategy_Cum_Returns'] = (1 + data['Strategy_Returns']).cumprod()
        data['BuyHold_Cum_Returns'] = (1 + data['Returns']).cumprod()
        
        # Risk metrics
        excess_returns = data['Strategy_Returns'] - 0.02/252  # Risk-free rate
        sharpe = np.sqrt(252) * excess_returns.mean() / excess_returns.std()
        
        negative_returns = data['Strategy_Returns'][data['Strategy_Returns'] < 0]
        sortino = np.sqrt(252) * excess_returns.mean() / negative_returns.std()
        
        # Drawdown analysis
        rolling_max = data['Strategy_Cum_Returns'].expanding().max()
        drawdowns = data['Strategy_Cum_Returns'] / rolling_max - 1
        max_drawdown = drawdowns.min()
        
        # Trading statistics
        trades = data['Position'].diff().fillna(0) != 0
        wins = data['Strategy_Returns'][trades] > 0
        
        return {
            'total_return': (data['Strategy_Cum_Returns'].iloc[-1] - 1) * 100,
            'benchmark_return': (data['BuyHold_Cum_Returns'].iloc[-1] - 1) * 100,
            'sharpe': sharpe,
            'sortino': sortino,
            'max_drawdown': max_drawdown * 100,
            'win_rate': (len(wins[wins]) / len(wins) if len(wins) > 0 else 0) * 100,
            'total_trades': len(wins),
            'returns_data': data[['Strategy_Cum_Returns', 'BuyHold_Cum_Returns']]
        }

def main():
    st.set_page_config(page_title="Brutal Trading Strategy", layout="wide")
    st.title("Trading Strategy Reality Check 🎯")
    
    # Sidebar configuration
    st.sidebar.header("Market Parameters")
    ticker = st.sidebar.text_input("Ticker Symbol", "SPY")
    start_date = st.sidebar.date_input("Start Date", datetime(2023, 1, 1))
    end_date = st.sidebar.date_input("End Date", datetime.now())
    
    st.sidebar.header("Advanced Analysis")
    params = {
        'n_regimes': st.sidebar.slider("Market Regimes", 2, 5, 3),
        'hmm_history': st.sidebar.slider("HMM Lookback (days)", 30, 252, 126),
        'hurst_window': st.sidebar.slider("Hurst Window", 10, 100, 50),
        'spectral_window': st.sidebar.slider("Spectral Window", 10, 100, 30),
        'position_size': st.sidebar.slider("Position Size (%)", 1, 100, 10),
        'max_drawdown_limit': st.sidebar.slider("Max Drawdown Limit (%)", 5, 30, 15)
    }
    
    if st.sidebar.button("Run Analysis"):
        with st.spinner("Analyzing market data..."):
            try:
                data = yf.download(ticker, start=start_date, end=end_date)
                if data.empty:
                    st.error("No data found. Check your ticker symbol.")
                    return
                
                executor = StrategyExecutor()
                metrics = executor.calculate_all_metrics(data, params)
                performance = executor.calculate_performance_metrics(data, params)
                
                # Market Analysis
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Market Regime", f"Regime {metrics['current_regime']}")
                with col2:
                    st.metric("Hurst Exponent", f"{metrics['hurst']:.2f}")
                with col3:
                    st.metric("Dominant Cycle", f"{metrics['dominant_cycle']:.2f} days")
                
                # Performance Metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Strategy Return", 
                             f"{performance['total_return']:.2f}%",
                             delta=f"{performance['total_return'] - performance['benchmark_return']:.2f}%")
                with col2:
                    st.metric("Sharpe Ratio", f"{performance['sharpe']:.2f}")
                with col3:
                    st.metric("Sortino Ratio", f"{performance['sortino']:.2f}")
                
                # Risk Metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Maximum Drawdown", f"{performance['max_drawdown']:.2f}%")
                with col2:
                    st.metric("Win Rate", f"{performance['win_rate']:.2f}%")
                with col3:
                    st.metric("Total Trades", performance['total_trades'])
                
                # Charts
                st.subheader("Strategy Performance")
                st.line_chart(performance['returns_data'])
                
                st.subheader("Market Regimes")
                regime_chart = pd.DataFrame({
                    'Price': data['Close'],
                    'Regime': metrics['regimes']
                })
                st.line_chart(regime_chart)
                
            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    main()

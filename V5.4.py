import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import scipy.stats
import scipy.signal
from datetime import datetime, timedelta
from typing import Dict, Tuple, List
from hmmlearn import hmm
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

class RiskManager:
    def __init__(self):
        self.max_drawdown_limit = -0.15  # 15% max drawdown
        self.position_size_limit = 0.25   # 25% max position
        self.var_limit = -0.02            # 2% Value at Risk limit
        
    def calculate_var(self, returns: pd.Series, confidence: float = 0.95) -> float:
        return np.percentile(returns, (1 - confidence) * 100)
    
    def calculate_cvar(self, returns: pd.Series, confidence: float = 0.95) -> float:
        var = self.calculate_var(returns, confidence)
        return returns[returns <= var].mean()
    
    def adjust_position_size(self, 
                           base_size: float, 
                           volatility: float, 
                           drawdown: float) -> float:
        # Reduce position size based on volatility and drawdown
        vol_adjustment = np.exp(-2 * volatility)
        dd_adjustment = np.exp(2 * drawdown) if drawdown > self.max_drawdown_limit else 1
        
        return min(base_size * vol_adjustment * dd_adjustment, self.position_size_limit)

class MarketAnalyzer:
    def __init__(self):
        self.scaler = StandardScaler()
        self.risk_manager = RiskManager()
        
    def calculate_advanced_metrics(self, data: pd.DataFrame) -> Dict:
        returns = data['Close'].pct_change()
        
        # Advanced volatility metrics
        realized_vol = returns.std() * np.sqrt(252)
        high_low_vol = np.log(data['High'] / data['Low']).std() * np.sqrt(252)
        
        # Market efficiency ratio
        price_path = np.sum(np.abs(data['Close'].diff()))
        direct_path = np.abs(data['Close'].iloc[-1] - data['Close'].iloc[0])
        efficiency_ratio = direct_path / price_path if price_path != 0 else 0
        
        return {
            'realized_volatility': realized_vol,
            'high_low_volatility': high_low_vol,
            'efficiency_ratio': efficiency_ratio,
            'var_95': self.risk_manager.calculate_var(returns),
            'cvar_95': self.risk_manager.calculate_cvar(returns)
        }

    def detect_market_regime(self, data: pd.DataFrame) -> str:
        returns = data['Close'].pct_change()
        vol = returns.rolling(21).std()
        
        current_vol = vol.iloc[-1]
        avg_vol = vol.mean()
        
        if current_vol > 2 * avg_vol:
            return "Crisis"
        elif current_vol > 1.5 * avg_vol:
            return "High Volatility"
        elif current_vol < 0.5 * avg_vol:
            return "Low Volatility"
        else:
            return "Normal"

class StrategyExecutor:
    def __init__(self):
        self.analyzer = MarketAnalyzer()
        self.risk_manager = RiskManager()
        self.trade_history = []
        
    def calculate_optimal_position(self, 
                                 data: pd.DataFrame, 
                                 signal: float,
                                 base_size: float) -> float:
        # Get current market conditions
        returns = data['Close'].pct_change()
        current_drawdown = (data['Close'] / data['Close'].expanding().max() - 1).iloc[-1]
        current_vol = returns.std()
        
        # Adjust position size based on risk metrics
        optimal_size = self.risk_manager.adjust_position_size(
            base_size=base_size,
            volatility=current_vol,
            drawdown=current_drawdown
        )
        
        return optimal_size * signal

    def execute_strategy(self, data: pd.DataFrame, params: Dict) -> Dict:
        """
        This is where the rubber meets the fucking road
        """
        metrics = self.analyzer.calculate_advanced_metrics(data)
        market_regime = self.analyzer.detect_market_regime(data)
        
        # Generate trading signals
        data['Signal'] = self.generate_signals(data, params)
        
        # Calculate position sizes with risk management
        data['Position'] = data['Signal'].apply(
            lambda x: self.calculate_optimal_position(
                data, x, params['position_size'] / 100
            )
        )
        
        # Calculate returns and metrics
        data['Strategy_Returns'] = data['Position'].shift(1) * data['Close'].pct_change()
        data['Cumulative_Returns'] = (1 + data['Strategy_Returns']).cumprod()
        
        return {
            'data': data,
            'metrics': metrics,
            'market_regime': market_regime
        }
      def main():
    st.set_page_config(page_title="No-Bullshit Trading Dashboard", layout="wide")
    
    # Header with brutal reality check
    st.title("Trading Reality Check Dashboard 🎯")
    st.markdown("""
    <style>
    .brutal-warning {
        color: red;
        font-weight: bold;
        padding: 10px;
        border: 2px solid red;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar with advanced controls
    with st.sidebar:
        st.header("Strategy Parameters")
        ticker = st.text_input("Ticker", "SPY")
        lookback = st.slider("Lookback Period (Days)", 30, 500, 252)
        
        # Advanced Risk Parameters
        st.subheader("Risk Management")
        risk_params = {
            'position_size': st.slider("Max Position Size (%)", 1, 100, 25),
            'stop_loss': st.slider("Stop Loss (%)", 1, 20, 5),
            'max_drawdown': st.slider("Max Drawdown (%)", 5, 30, 15),
            'var_confidence': st.slider("VaR Confidence (%)", 90, 99, 95)
        }
        
        # Market Regime Detection
        st.subheader("Market Regime Detection")
        regime_params = {
            'vol_window': st.slider("Volatility Window", 5, 50, 21),
            'regime_threshold': st.slider("Regime Change Threshold", 1.0, 3.0, 1.5)
        }

    if st.sidebar.button("Analyze Market"):
        try:
            # Load and analyze data
            end_date = datetime.now()
            start_date = end_date - timedelta(days=lookback)
            data = yf.download(ticker, start=start_date, end=end_date)
            
            if data.empty:
                st.error("No data found. Check your ticker symbol.")
                return
            
            # Execute strategy
            executor = StrategyExecutor()
            results = executor.execute_strategy(data, {**risk_params, **regime_params})
            
            # Performance Dashboard
            col1, col2, col3, col4 = st.columns(4)
            
            total_return = (results['data']['Cumulative_Returns'].iloc[-1] - 1) * 100
            sharpe = results['metrics']['realized_volatility']
            max_dd = results['data']['Cumulative_Returns'].min() * 100
            
            with col1:
                st.metric("Total Return", 
                         f"{total_return:.2f}%",
                         f"VaR: {results['metrics']['var_95']:.2f}%")
            with col2:
                st.metric("Sharpe Ratio",
                         f"{sharpe:.2f}",
                         f"Vol: {results['metrics']['realized_volatility']:.2f}")
            with col3:
                st.metric("Max Drawdown",
                         f"{max_dd:.2f}%",
                         f"CVaR: {results['metrics']['cvar_95']:.2f}%")
            with col4:
                st.metric("Market Regime",
                         results['market_regime'],
                         f"Efficiency: {results['metrics']['efficiency_ratio']:.2f}")

            # Brutal Reality Check
            if total_return < 0:
                st.markdown("""
                <div class='brutal-warning'>
                🚨 Your strategy is losing money. Either fix it or stop trading.
                </div>
                """, unsafe_allow_html=True)
            elif sharpe < 1:
                st.markdown("""
                <div class='brutal-warning'>
                ⚠️ Your risk-adjusted returns are garbage. You'd do better buying bonds.
                </div>
                """, unsafe_allow_html=True)

            # Advanced Visualization
            fig = make_subplots(rows=3, cols=1,
                              shared_xaxis=True,
                              vertical_spacing=0.05,
                              subplot_titles=('Price & Positions',
                                            'Market Regime',
                                            'Strategy Performance'))

            # Price and Position Plot
            fig.add_trace(
                go.Scatter(x=data.index, y=data['Close'],
                          name='Price', line=dict(color='blue')),
                row=1, col=1
            )

            # Position heat map
            fig.add_trace(
                go.Scatter(x=results['data'].index,
                          y=data['Close'],
                          name='Position Size',
                          mode='markers',
                          marker=dict(
                              size=10,
                              color=results['data']['Position'],
                              colorscale='RdYlGn',
                              showscale=True
                          )),
                row=1, col=1
            )

            # Market Regime Plot
            fig.add_trace(
                go.Scatter(x=data.index,
                          y=results['data']['Strategy_Returns'].rolling(21).std(),
                          name='Volatility Regime',
                          line=dict(color='orange')),
                row=2, col=1
            )

            # Performance Plot
            fig.add_trace(
                go.Scatter(x=data.index,
                          y=results['data']['Cumulative_Returns'],
                          name='Strategy Returns',
                          line=dict(color='green')),
                row=3, col=1
            )

            fig.update_layout(height=800, showlegend=True)
            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    main()

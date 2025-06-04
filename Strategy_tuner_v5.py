import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from hmmlearn.hmm import GaussianHMM
from scipy.signal import welch
import matplotlib.pyplot as plt
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")
st.title("📈 Strategy Tuner v5 - No BS Edition")

# Sidebar Controls
with st.sidebar:
    st.header("Strategy Parameters")
    ticker = st.text_input("Asset Ticker", "SPY", help="Enter any valid ticker (e.g., SPY, QQQ, BTC-USD)")
    start_date = st.date_input("Start Date", pd.to_datetime("2010-01-01"))
    end_date = st.date_input("End Date", datetime.today())
    
    st.subheader("Model Configuration")
    rolling_window = st.slider("Rolling Window (Days)", 100, 500, 252)
    hurst_window = st.slider("Hurst Window", 20, 100, 50)
    vol_target = st.slider("Volatility Target (%)", 5, 30, 15)
    max_leverage = st.slider("Max Leverage", 0.0, 3.0, 1.0)
    
    st.subheader("Risk Management")
    drawdown_limit = st.slider("Drawdown Kill Switch (%)", 5, 30, 15)
    consecutive_loss_limit = st.slider("Max Consecutive Losses", 3, 10, 5)
    
    st.subheader("Trading Costs")
    slippage_pct = st.slider("Slippage (%)", 0.0, 1.0, 0.1)
    commission_pct = st.slider("Commission (%)", 0.0, 1.0, 0.05)

def load_data(ticker_symbol, start, end):
    """Load and validate price data with proper error handling"""
    try:
        df = yf.download(ticker_symbol, start=start, end=end, auto_adjust=True)
        if df.empty:
            st.error(f"No data found for {ticker_symbol}. Check the ticker symbol.")
            return None
        df['Price'] = df['Close']
        df['LogReturn'] = np.log(df['Price'] / df['Price'].shift(1))
        return df.dropna()
    except Exception as e:
        st.error(f"Failed to load {ticker_symbol}. Error: {str(e)}")
        return None

def hurst(ts):
    """Calculate Hurst exponent using log-log regression"""
    lags = range(2, min(20, len(ts)//2))
    tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags]
    reg = np.polyfit(np.log(lags), np.log(tau), 1)
    return reg[0]

def rolling_hmm_regime(returns, window=252):
    """Forward-walking HMM regime detection"""
    regimes = []
    probs = []
    
    for t in range(window, len(returns)):
        X = returns[t-window:t].values.reshape(-1, 1)
        hmm = GaussianHMM(n_components=3, n_iter=1000, random_state=42)
        hmm.fit(X)
        
        # Classify regimes based on mean and volatility
        means = hmm.means_.flatten()
        vols = np.sqrt(np.diag(hmm.covars_[0]))
        
        # Identify regimes
        bull = np.argmax(means)
        bear = np.argmin(means)
        chop = list(set(range(3)) - set([bull, bear]))[0]
        
        # Get current regime and probability
        curr_x = returns.iloc[t:t+1].values.reshape(-1, 1)
        curr_regime = hmm.predict(curr_x)[0]
        curr_prob = np.max(hmm.predict_proba(curr_x))
        
        # Map to strategy regime
        if curr_regime == bull and curr_prob > 0.6:
            regimes.append(1)
        elif curr_regime == bear and curr_prob > 0.6:
            regimes.append(-1)
        else:
            regimes.append(0)
        
        probs.append(curr_prob)
            
    return pd.Series(regimes, index=returns.index[window:]), pd.Series(probs, index=returns.index[window:])

def position_sizer(regime, vol, prob, hurst_val):
    """Dynamic position sizing based on regime confidence and market conditions"""
    vol_scalar = vol_target/100 / (vol * np.sqrt(252))
    regime_scalar = {1: 1.0, -1: -1.0, 0: 0.0}[regime]
    
    # Scale position by regime probability and trend strength
    confidence = prob * min(max(hurst_val - 0.5, 0), 0.5) * 2
    
    position = regime_scalar * vol_scalar * confidence
    return np.clip(position, -max_leverage, max_leverage)

# Main Strategy Execution
df = load_data(ticker, start_date, end_date)
if df is None:
    st.stop()

try:
    # Initialize forward-walking analysis
    df['Regime'] = np.nan
    df['RegimeProb'] = np.nan
    df['Position'] = 0.0
    df['Hurst'] = np.nan
    
    # Calculate rolling metrics
    returns_subset = df['LogReturn'].copy()
    df['Volatility'] = returns_subset.rolling(21).std()
    
    # Forward walk with rolling windows
    valid_idx = df.index[rolling_window:]
    df.loc[valid_idx, 'Regime'], df.loc[valid_idx, 'RegimeProb'] = \
        rolling_hmm_regime(returns_subset, rolling_window)
    
    # Rolling Hurst calculation
    hurst_values = []
    for t in range(hurst_window, len(df)):
        h = hurst(returns_subset.iloc[t-hurst_window:t])
        hurst_values.append(h)
    df.loc[df.index[hurst_window:], 'Hurst'] = hurst_values
    
    # Forward walk portfolio
    equity = []
    capital = 1.0
    max_capital = 1.0
    current_pos = 0.0
    consecutive_losses = 0
    trade_log = []
    
    for i in range(max(rolling_window, hurst_window), len(df)):
        # Check kill switches
        drawdown = (max_capital - capital) / max_capital
        if drawdown > drawdown_limit/100 or consecutive_losses >= consecutive_loss_limit:
            st.warning(f"Kill switch activated at {df.index[i].date()}")
            break
            
        # Get current signals
        regime = df['Regime'].iloc[i]
        prob = df['RegimeProb'].iloc[i]
        vol = df['Volatility'].iloc[i]
        hurst_val = df['Hurst'].iloc[i]
        
        # Size position
        target_pos = position_sizer(regime, vol, prob, hurst_val)
        
        # Execute if significant position change
        if abs(target_pos - current_pos) > 0.01:
            capital *= (1 - (slippage_pct + commission_pct)/100)
            trade_log.append((df.index[i], current_pos, target_pos))
            current_pos = target_pos
        
        # Update capital
        returns = df['LogReturn'].iloc[i]
        prev_capital = capital
        capital *= np.exp(current_pos * returns)
        
        # Track consecutive losses
        if capital < prev_capital:
            consecutive_losses += 1
        else:
            consecutive_losses = 0
            
        max_capital = max(capital, max_capital)
        equity.append(capital)
        df.loc[df.index[i], 'Position'] = current_pos
    
    # Performance analysis and visualization
    df = df.iloc[max(rolling_window, hurst_window):].copy()
    df['Equity'] = equity
    
    # Plot equity curve with regime overlay
    st.subheader("📈 Strategy Performance")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), height_ratios=[3, 1])
    
    # Equity curve
    df['Equity'].plot(ax=ax1, label="Strategy", color='blue')
    (df['Price']/df['Price'].iloc[0]).plot(ax=ax1, label="Buy & Hold", alpha=0.4)
    
    # Regime overlay
    for regime, color, label in zip([1, -1, 0], ['green', 'red', 'gray'], ['Bull', 'Bear', 'Chop']):
        mask = df['Regime'] == regime
        if mask.any():
            ax1.fill_between(df.index, 0, df['Equity'].max(), 
                           where=mask, alpha=0.1, color=color, label=label)
    
    ax1.legend()
    ax1.set_title("Equity Curve & Market Regimes")
    
    # Position size
    df['Position'].plot(ax=ax2, color='purple', label='Position Size')
    ax2.set_title("Position Sizing")
    ax2.legend()
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Performance metrics
    st.subheader("📊 Strategy Metrics")
    total_return = df['Equity'].iloc[-1] - 1
    sharpe = np.sqrt(252) * df['Equity'].pct_change().mean() / df['Equity'].pct_change().std()
    max_dd = (1 - df['Equity'] / df['Equity'].cummax()).max()
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Return", f"{total_return:.2%}")
    col2.metric("Sharpe Ratio", f"{sharpe:.2f}")
    col3.metric("Max Drawdown", f"{max_dd:.2%}")
    col4.metric("# Trades", len(trade_log))
    
    # Trade log
    st.subheader("📋 Trade History")
    trade_df = pd.DataFrame(trade_log, columns=["Date", "From", "To"]).set_index("Date")
    st.dataframe(trade_df)

except Exception as e:
    st.error(f"Strategy execution failed: {str(e)}")

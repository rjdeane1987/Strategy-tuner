import streamlit as st
import pandas as pd
import numpy as np
from hmmlearn import hmm
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_data(ticker, start_date, end_date):
    try:
        df = yf.download(ticker, start=start_date, end=end_date)
        df['LogReturn'] = np.log(df['Close'] / df['Close'].shift(1))
        return df
    except Exception as e:
        st.error(f"Data fetch failed: {e}")
        return None

def fit_hmm(X):
    best_score = float('-inf')
    best_model = None
    
    for _ in range(3):  # Multiple attempts for robust fitting
        model = hmm.GaussianHMM(n_components=3, covariance_type="full", n_iter=2000, tol=1e-6)
        model.fit(X.reshape(-1, 1))
        score = model.score(X.reshape(-1, 1))
        
        if score > best_score:
            best_score = score
            best_model = model
    
    return best_model

def calculate_position(regime, prob, vol, vol_target, max_leverage):
    regime_scalar = {1: 1.0, -1: -1.0, 0: 0.0}[regime]
    vol_scalar = vol_target/100 / (vol * np.sqrt(252))
    confidence = (prob - 0.33) / 0.67  # Normalized probability
    position = regime_scalar * vol_scalar * confidence
    return np.clip(position, -max_leverage, max_leverage)

def run_strategy(df, window_size, vol_target, max_leverage, max_drawdown, max_consecutive_losses):
    positions = []
    regimes = []
    equity = [1.0]
    consecutive_losses = 0
    max_capital = 1.0
    
    # Calculate rolling volatility
    df['Volatility'] = df['LogReturn'].rolling(window=21).std()
    
    for i in range(window_size, len(df)):
        returns = df['LogReturn'].iloc[i-window_size:i]
        vol = df['Volatility'].iloc[i]
        
        model = fit_hmm(returns.values)
        means = model.means_.flatten()
        curr_return = df['LogReturn'].iloc[i]
        curr_prob = model.predict_proba(curr_return.reshape(1, -1))[0]
        curr_regime = model.predict(curr_return.reshape(1, -1))[0]
        
        # Regime assignment with probability threshold
        if curr_regime == np.argmax(means) and curr_prob.max() > 0.7:
            regime = 1  # Bull
        elif curr_regime == np.argmin(means) and curr_prob.max() > 0.7:
            regime = -1  # Bear
        else:
            regime = 0  # Chop
            
        position = calculate_position(regime, curr_prob.max(), vol, vol_target, max_leverage)
        
        # Capital update with transaction costs
        if len(positions) > 0 and abs(position - positions[-1]) > 0.01:
            equity[-1] *= 0.9985  # Combined slippage and commission
        
        # Strategy returns calculation
        strategy_return = position * df['LogReturn'].iloc[i]
        new_capital = equity[-1] * np.exp(strategy_return)
        
        # Kill switch logic
        drawdown = (max_capital - new_capital) / max_capital
        if drawdown > max_drawdown/100:
            st.warning(f"Drawdown kill switch activated at {drawdown:.2%}")
            break
            
        if strategy_return < 0:
            consecutive_losses += 1
        else:
            consecutive_losses = 0
            
        if consecutive_losses > max_consecutive_losses:
            st.warning("Consecutive losses kill switch activated")
            break
            
        equity.append(new_capital)
        max_capital = max(max_capital, new_capital)
        positions.append(position)
        regimes.append(regime)
    
    # Performance metrics with CORRECT Sharpe calculation
    df_results = pd.DataFrame({
        'Position': positions,
        'Regime': regimes,
        'Equity': equity[1:],
        'Strategy_Returns': [pos * ret for pos, ret in zip(positions, df['LogReturn'].iloc[window_size:])]
    })
    
    total_return = df_results['Equity'].iloc[-1] - 1
    strategy_sharpe = np.sqrt(252) * df_results['Strategy_Returns'].mean() / df_results['Strategy_Returns'].std()
    max_dd = (1 - df_results['Equity'] / df_results['Equity'].cummax()).max()
    
    return df_results, total_return, strategy_sharpe, max_dd

# Streamlit UI
st.title('Regime-Switching Strategy Backtester')

# Input parameters
col1, col2 = st.columns(2)
with col1:
    ticker = st.text_input('Ticker', 'SPY')
    start_date = st.date_input('Start Date')
    window_size = st.slider('Window Size', 30, 252, 126)
    vol_target = st.slider('Volatility Target (%)', 5, 50, 20)

with col2:
    end_date = st.date_input('End Date')
    max_leverage = st.slider('Max Leverage', 0.1, 3.0, 1.0)
    max_drawdown = st.slider('Max Drawdown (%)', 5, 50, 20)
    max_consecutive_losses = st.slider('Max Consecutive Losses', 3, 20, 10)

if st.button('Run Backtest'):
    df = fetch_data(ticker, start_date, end_date)
    if df is not None:
        results, total_return, sharpe, max_dd = run_strategy(
            df, window_size, vol_target, max_leverage, 
            max_drawdown, max_consecutive_losses
        )
        
        # Results display
        st.write(f"Total Return: {total_return:.2%}")
        st.write(f"Sharpe Ratio: {sharpe:.2f}")
        st.write(f"Max Drawdown: {max_dd:.2%}")
        
        # Visualization
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        ax1.plot(results.index, results['Equity'])
        ax1.set_title('Equity Curve')
        
        ax2.plot(results.index, results['Position'])
        ax2.set_title('Position Size')
        st.pyplot(fig)

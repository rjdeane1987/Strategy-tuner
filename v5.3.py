import yfinance as yf
import pandas as pd
import numpy as np
import talib
import logging
from hmmlearn import hmm
from sklearn.base import BaseEstimator
from typing import Dict, Tuple, List
from datetime import datetime
import streamlit as st

# Set up Streamlit
st.set_page_config(page_title="Trading Strategy Tuner", layout="wide")
st.title("Trading Strategy Tuner 🚀")
st.sidebar.header("Configuration")

class StrategyTunerConfig:
    def __init__(self):
        self.BATCH_SIZE = 100
        self.LEARNING_RATE = 0.01
        self.N_REGIMES = 3
        self.LOOKBACK_PERIOD = 252

class StrategyTuner(BaseEstimator):
    def __init__(self, config: StrategyTunerConfig):
        self.config = config
        self.regime_model = self._initialize_regime_model()
        self.history = []
        
    def _initialize_regime_model(self) -> hmm.GaussianHMM:
        return hmm.GaussianHMM(
            n_components=self.config.N_REGIMES,
            covariance_type="full",
            n_iter=100
        )

    def _train_iteration(self, data: pd.DataFrame) -> float:
        try:
            regimes, regime_confidence = self._detect_market_regime(data)
            action_score = self._contains_actionable_items(data)
            execution_score = self._has_concrete_steps(data)
            
            adjusted_action = self._adjust_signals_for_regime(action_score, regime_confidence)
            adjusted_execution = self._adjust_signals_for_regime(execution_score, regime_confidence)
            
            final_score = (adjusted_action * 0.6 + adjusted_execution * 0.4)
            self.history.append(final_score)
            
            return final_score
            
        except Exception as e:
            logger.error(f"Training iteration failed: {str(e)}")
            raise

    def _detect_market_regime(self, data: pd.DataFrame) -> Tuple[np.ndarray, float]:
        try:
            returns = np.column_stack([
                data['Close'].pct_change().fillna(0),
                data['Volume'].pct_change().fillna(0),
                data['High'].div(data['Low']).pct_change().fillna(0)
            ])
            
            self.regime_model.fit(returns)
            regimes = self.regime_model.predict(returns)
            
            current_regime = regimes[-1]
            regime_probs = self.regime_model.predict_proba(returns)
            regime_confidence = regime_probs[-1][current_regime]
            
            return regimes, regime_confidence
            
        except Exception as e:
            logger.error(f"Regime detection failed: {str(e)}")
            return np.zeros(len(data)), 0.0

    def _contains_actionable_items(self, data: pd.DataFrame) -> float:
        try:
            signals = {
                'price_crossovers': self._check_moving_average_crossovers(data),
                'volume_spikes': self._check_volume_anomalies(data),
                'momentum_shifts': self._calculate_momentum_signals(data),
                'support_resistance': self._identify_key_levels(data),
                'volatility_triggers': self._measure_volatility_breakouts(data)
            }
            
            weights = {
                'price_crossovers': 0.3,
                'volume_spikes': 0.2,
                'momentum_shifts': 0.2,
                'support_resistance': 0.15,
                'volatility_triggers': 0.15
            }
            
            score = sum(signal * weights[signal_type] 
                       for signal_type, signal in signals.items())
            
            return max(min(score, 1.0), 0.0)
            
        except Exception as e:
            logger.error(f"Signal analysis failed: {str(e)}")
            return 0.0

    def _has_concrete_steps(self, data: pd.DataFrame) -> float:
        try:
            execution_criteria = {
                'position_size': self._calculate_position_size(data),
                'risk_ratio': self._calculate_risk_reward_ratio(data),
                'market_conditions': self._evaluate_market_conditions(data),
                'entry_precision': self._measure_entry_quality(data),
                'exit_clarity': self._evaluate_exit_conditions(data)
            }
            
            score = sum(execution_criteria.values()) / len(execution_criteria)
            risk_multiplier = self._calculate_risk_multiplier(data)
            
            return max(min(score * risk_multiplier, 1.0), 0.0)
            
        except Exception as e:
            logger.error(f"Execution analysis failed: {str(e)}")
            return 0.0

    def _adjust_signals_for_regime(self, base_signal: float, regime_confidence: float) -> float:
        return base_signal * (0.5 + regime_confidence)

    def _check_moving_average_crossovers(self, data: pd.DataFrame) -> float:
        try:
            data['SMA20'] = talib.SMA(data['Close'], timeperiod=20)
            data['SMA50'] = talib.SMA(data['Close'], timeperiod=50)
            data['EMA12'] = talib.EMA(data['Close'], timeperiod=12)
            data['EMA26'] = talib.EMA(data['Close'], timeperiod=26)
            
            golden_cross = (data['SMA20'] > data['SMA50']) & (data['SMA20'].shift(1) <= data['SMA50'].shift(1))
            death_cross = (data['SMA20'] < data['SMA50']) & (data['SMA20'].shift(1) >= data['SMA50'].shift(1))
            
            score = (
                sum(golden_cross.tail(5)) * 0.3 +
                sum(death_cross.tail(5)) * 0.3 +
                abs(data['EMA12'] - data['EMA26']).tail(1).values[0] / data['Close'].tail(1).values[0] * 0.4
            )
            
            return min(score, 1.0)
            
        except Exception as e:
            logger.error(f"MA crossover analysis failed: {str(e)}")
            return 0.0

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('strategy_tuner.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    # User inputs
    ticker = st.sidebar.text_input("Enter Ticker Symbol", "SPY")
    start_date = st.sidebar.date_input("Start Date", datetime(2023, 1, 1))
    end_date = st.sidebar.date_input("End Date", datetime.now())
    
    if st.sidebar.button("Run Analysis"):
        with st.spinner("Running strategy analysis..."):
            try:
                # Load data
                data = yf.download(ticker, start=start_date, end=end_date)
                
                # Initialize and run strategy
                tuner = StrategyTuner(StrategyTunerConfig())
                
                # Market Regime Analysis
                regimes, confidence = tuner._detect_market_regime(data)
                st.subheader("Market Regime Analysis")
                st.metric("Regime Confidence", f"{confidence:.2%}")
                
                # Strategy Scores
                score = tuner._train_iteration(data)
                st.subheader("Strategy Performance")
                st.metric("Strategy Score", f"{score:.2%}")
                
                # Plot the data
                st.line_chart(data['Close'])
                
            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    main()

import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class MarketLSTM(nn.Module):
    def __init__(self, input_size, hidden_layer_size, output_size):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size
        self.lstm = nn.LSTM(input_size, hidden_layer_size, batch_first=True)
        self.linear = nn.Linear(hidden_layer_size, output_size)

    def forward(self, input_seq):
        lstm_out, _ = self.lstm(input_seq)
        predictions = self.linear(lstm_out[:, -1, :])
        return predictions

def train_market_model(data: pd.DataFrame):
    """
    Mock training function.
    In real implementation, iter over data, scale with MinMaxScaler, sequence it, and run epochs.
    """
    model = MarketLSTM(input_size=3, hidden_layer_size=50, output_size=1)
    return model

def predict_crop_market(model, current_price, current_demand, current_supply, farming_cost_per_ton):
    """
    Mock inference function.
    Given current price, demand, and supply, predict a trajectory.
    Returns: Future Price, Profit Estimate, Best Selling Date
    """
    model.eval()
    
    # Mock some future simulated price array
    base = current_price if current_price else 1000
    noise = np.random.normal(0, base * 0.05, 30) # 30 days
    trend = np.linspace(0, (current_demand - current_supply) * 0.1, 30)
    future_prices = base + noise + trend
    
    best_day_idx = np.argmax(future_prices)
    best_price = future_prices[best_day_idx]
    
    future_date = datetime.utcnow() + timedelta(days=int(best_day_idx))
    profit_estimate = best_price - farming_cost_per_ton
    
    return {
        "future_price_curve": future_prices.tolist(),
        "peak_future_price": float(best_price),
        "best_selling_date": future_date,
        "profit_estimate": float(profit_estimate)
    }

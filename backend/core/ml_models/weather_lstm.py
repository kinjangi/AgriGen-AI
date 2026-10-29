import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class WeatherLSTM(nn.Module):
    def __init__(self, input_size, hidden_layer_size, output_size):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size
        self.lstm = nn.LSTM(input_size, hidden_layer_size, batch_first=True)
        self.linear = nn.Linear(hidden_layer_size, output_size)

    def forward(self, input_seq):
        lstm_out, _ = self.lstm(input_seq)
        predictions = self.linear(lstm_out[:, -1, :])
        return predictions

def train_weather_model(data: pd.DataFrame):
    """
    Mock training function.
    In real implementation, iter over data, scale with MinMaxScaler, sequence it, and run epochs.
    """
    model = WeatherLSTM(input_size=4, hidden_layer_size=50, output_size=4)
    # mock train loop
    return model

def predict_weather(model, recent_data: np.ndarray, steps=7):
    """
    Mock inference function.
    Returns np.ndarray of shape (steps, 4) for (temp, humidity, precipitation, wind_speed)
    """
    model.eval()
    with torch.no_grad():
        # Mocking 7 days of predictions
        # Normally would autoregressively feed predictions back to LSTM
        mock_output = np.random.rand(steps, 4) * [35, 100, 20, 15] # scaling random to roughly standard values
    return mock_output

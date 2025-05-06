from joblib import load
import os

x_scaler = load(os.path.join(os.getcwd(), 'artifacts','x_scaler.pkl'))
y_scaler = load(os.path.join(os.getcwd(), 'artifacts','y_scaler.pkl'))

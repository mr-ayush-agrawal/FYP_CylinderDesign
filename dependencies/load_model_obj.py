from joblib import load
import os

model = load(os.path.join(os.getcwd(), 'artifacts','final_model.pkl'))

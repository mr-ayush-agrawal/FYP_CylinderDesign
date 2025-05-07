from joblib import load
import os

model = load(os.path.join(os.getcwd(), 'artifacts','wrng_model.pkl'))

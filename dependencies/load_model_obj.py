from joblib import load
import os

from dependencies.utils.loss_utils import loss_function
model = load(os.path.join(os.getcwd(), 'artifacts','wrng_model.pkl'))

"""
This package is responsible for making callback fucntions available for the app
"""
import bentoml
# model = bentoml.keras.load_model('lstm_finance:latest')
BASE_URL = "https://lstm-predict.run-us-west2.goorm.io/predict"
from .event_handler import *
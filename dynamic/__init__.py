import bentoml
# model = bentoml.keras.load_model('lstm_finance:latest')
BASE_URL = "https://lstm-predictor.run-us-west2.goorm.io/predict" 
from .event_handler import *
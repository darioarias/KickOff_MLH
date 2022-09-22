import bentoml
model = bentoml.keras.load_model('lstm_finance:latest')
from .event_handler import *
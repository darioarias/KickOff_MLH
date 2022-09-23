import json
import yfinance as yf
import requests
from .stock_data import supported_stock
from . import BASE_URL
from .ml_support import normalize

def query_features(ticker, *features, testing = False, file=""):
  if testing:
    print('SERVING STATIC DATA')
    file = file or "info.json"
    with open(file, mode='r', encoding='utf-8') as file:
      ticker_info = json.load(file)
  else: 
    ticker_info = yf.Ticker(ticker).info
  return [ticker_info[attr] for attr in features]


def stock_on_change(state):
  if state['stock'] == 'select':
    if 'prediction' in state:
      del state['prediction']
    return 

  features_label = ["open", "dayHigh", "dayLow", "volume", "currentPrice"]
  features = query_features(state['stock'], *features_label)
  

  # prediction = model.predict(normalize(features[:-1]))[0][0]

  # prediction = model.predict(normalize(features[:-1]))[0][0]
  data = requests.post(
    BASE_URL,
    headers={"content-type": "application/json"}, 
    data=f"{[[[n for n in normalize(features[:-1])[0][0]]]]}"
  ).json()
  
  # features_label.append('prediction')
  features.append(float(data[0][0]))
  # print("DATRA", data)
  
  # result = {}
  # for label, val in zip(features_label, features):
  #   result[label] = val

  state['prediction'] = features

def stock_name_format(ticket):
  return supported_stock[ticket]
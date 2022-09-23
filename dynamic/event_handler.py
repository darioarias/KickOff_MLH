"""
Creates the callbacks using all of the resources it needs
"""

import json
import yfinance as yf
import requests
from .stock_data import supported_stock
from . import BASE_URL
from .ml_support import normalize



def query_features(ticker, *features, testing = False, file=""):
  """ Makes an api call to yahoo finance, serves static data when testing is true. A file can be specified for static data as well"""
  if testing:
    print('SERVING STATIC DATA')
    file = file or "info.json"
    with open(file, mode='r', encoding='utf-8') as file:
      ticker_info = json.load(file)
  else: 
    ticker_info = yf.Ticker(ticker).info
  return [ticker_info[attr] for attr in features]


def stock_on_change(state):
  """ 'Listen' for user's selections and updates the app's state """
  if state['stock'] == 'select':
    if 'prediction' in state:
      del state['prediction']
    return 
  # the features we can to get from the api
  features_label = ["open", "dayHigh", "dayLow", "volume", "currentPrice"]
  features = query_features(state['stock'], *features_label)  # calls the api with the features it wants
  
  # makes an api request to the model using the data from yahoo finance
  data = requests.post(
    BASE_URL,
    headers={"content-type": "application/json"}, 
    data=f"{[[[n for n in normalize(features[:-1])[0][0]]]]}"
  ).json()
  
  # adds the result to the list
  features.append(float(data[0][0]))

  # update the state
  state['prediction'] = features

def stock_name_format(ticket):
  """ Update the name that will be displayed as stock choices"""
  return supported_stock[ticket]
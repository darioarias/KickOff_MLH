""" Provides support for quering the model """

from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

scaler = MinMaxScaler(feature_range=(0,1))
features = ['Open', 'High', 'Low', 'Volume']

with open("CSV/MSFT_kaggle.csv", mode='r', encoding='utf-8') as data:
  msft_data = pd.read_csv(data, na_values=['null'], index_col='Date', parse_dates=True, infer_datetime_format=True)
  scaler.fit(msft_data[['Open', 'High', 'Low', 'Volume']])

def normalize(point, scaler=scaler):
  """ Define how to scale values so the model can use them """
  transformed = scaler.transform([point])
  feature_transform = pd.DataFrame(columns=features, data=transformed)
  nparr = np.array(feature_transform)
  return nparr.reshape(feature_transform.shape[0], 1, feature_transform.shape[1])

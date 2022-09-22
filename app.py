import streamlit as st
import pandas as pd
from dynamic import stock_on_change, supported_stock, stock_name_format

st.title("Stock Closing Price Forecast")

st.header("About")

st.subheader("The Dataset")
st.markdown("""
This app uses a machine learning model to predict today's closing price of a given stock. 
The model is trained on historical data of the Microsoft stock (NYSE: MSFT), starting when 
the company went public in 1986 to March of 2022.

Below is a sneak peek of the dataset used to train the model:
""")
microsoft_df = pd.read_csv('CSV/MSFT_kaggle.csv', index_col='Date', thousands=',')
st.write(microsoft_df.tail(5))
st.markdown("""
In this dataset, `Open`, `High`, `Low`, and `Close` are the opening, highest, lowest, and 
closing prices of the stock on a given day. `Volume` is the number of shares traded on that
day. `Adj Close` is the closing price adjusted for stock splits and dividends.
""")

st.subheader("The Model")
st.markdown("""
The model is a Long Short-Term Memory (LSTM) neural network. It is a type of recurrent neural
network (RNN) that is able to remember information from previous time steps. LSTM is widely 
used to analyze time-series data, such as stock prices, because it allows the model to learn 
from past data to make predictions about future data.

The dataset is split 90:10 into training and testing data, respectively. The model is trained 
on the training data and then tested on the testing data. The graph below shows the model's 
predictions on the testing data. The blue line is the actual closing price of the stock, and 
the orange line is the predicted closing price of the stock.
""")
st.image("images/lstm_predictions.png", use_column_width=True)
st.markdown("""
This graph provides us a sense of the model's accuracy. At the moment, the model is able to 
predict the general trend of the stock's closing prices but overestimates the magnitude of 
the price changes. We will continue to fine-tune the model in the future.
""")

# Interaction Part
st.header("Predictions")
st.markdown("""
Select a stock from the dropdown to see the model's prediction for its closing price today.
""")

option = st.selectbox (
  'Which stock would you like to predict today\'s closing price?',
  supported_stock,
  key="stock",
  on_change=stock_on_change,
  args=[st.session_state],
  format_func=stock_name_format
)

if st.session_state.get('prediction', None):
  st.write(f'You want to learn about: {option}')
  st.write(st.session_state['prediction'])
  del st.session_state['prediction']



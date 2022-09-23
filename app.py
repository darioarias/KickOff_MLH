# imports
import streamlit as st
import pandas as pd
from dynamic import stock_on_change, supported_stock, stock_name_format

# start of steamlit, title the pafe
st.title("Stock Closing Price Forecast")

# set up headings as well
st.subheader("The Dataset")
# first part of the page
st.markdown("""
This app uses a machine learning model to predict today's closing price of a given stock. If
the market has closed for the day, the model will predict tomorrow's closing price.

The model is trained on historical data of the Microsoft stock (NYSE: MSFT), starting when 
the company went public in 1986 to March of 2022.

Below is a sneak peek of the dataset used to train the model:
""")

# bring in the data to show in the steamlit app
microsoft_df = pd.read_csv('CSV/MSFT_kaggle.csv', index_col='Date', thousands=',')
st.write(microsoft_df.tail(100))
# describe the data
st.markdown("""
In this dataset, `Open`, `High`, `Low`, and `Close` are the opening, highest, lowest, and 
closing prices of the stock on a given day. `Volume` is the number of shares traded on that
day. `Adj Close` is the closing price adjusted for stock splits and dividends.
""")

# adding another section
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

# showing an image
st.image("images/LSTM_predictions.png", use_column_width=True)
# describing an images
st.markdown("""
This graph provides us a sense of the model's accuracy. At the moment, the model is able to 
predict the general trend of the stock's closing prices but overestimates the magnitude of 
the price changes. We will continue to fine-tune the model in the future.

After the model has been trained, we saved it with BentoML API to its model store (a 
directory managed by BentoML). The model is then loaded from the model store every time you
select a stock from the dropdown menu below.
""")

# Interaction Part
st.header("Predictions")
st.markdown(""" In this section you can interact with the model and see prediction realtime.
Select a stock from the dropdown to see the model's prediction for its closing price today.
""")

# user can pick a stock 
option = st.selectbox (
  'Which stock would you like to predict today\'s closing price?',
  supported_stock,
  key="stock",
  on_change=stock_on_change,
  args=[st.session_state],
  format_func=stock_name_format
)

# placeholders only
open = 0
high = 0
low = 0
volume = 0
# adj_close = 0
# prev_close = 0
# close_change = 0
current_price = 0
prediction = 0

# update the page when the app detects predictions
if st.session_state.get('prediction', None):
  st.caption(f'For more details, visit [{option}](https://finance.yahoo.com/quote/{option}) on Yahoo Finance.')
  # st.write(st.session_state['prediction'])
  open, high, low, volume, current_price, prediction =\
    st.session_state['prediction']
  # print(st.session_state['prediction'])
  del st.session_state['prediction']


# dashboard
col1, col2, col3 = st.columns(3)
col1.metric("Open", "${:.2f}".format(open))
col2.metric("High", "${:.2f}".format(high))
col3.metric("Low", "${:.2f}".format(low))

col4, col5, col6 = st.columns(3)
col4.metric("Volume", "{:,}".format(volume))
col5.metric("Predicted Close", "${:.2f}".format(prediction), 
f' {"{0:.2%}".format((prediction/open)-1)} vs Open' if open != 0 else "")

st.header("About Us")
st.markdown("""
This app was created by [Dario Arias](https://github.com/darioarias) and [Quan Nguyen](https://github.com/quandollar). We are Fellows in the Open Source Program of the [MLH 
Fellowship](https://fellowship.mlh.io/). We created this project as part of the fellowship's
hackathon and to learn more about [BentoML](https://github.com/bentoml/BentoML), a machine
learning platform for saving and deploying models that we will be working with during our 
fellowship.

Dario is a Computer Science Senior at the City University of New York, Hunter College. 
Outside of school and the MLH Fellowship, he works part-time as a sailing instructor at Hudson River Community Sailing, 
and enjoys outdoor activities.

Quan is a Computer Science grad student in the MCIT program at the University of Pennsylvania. 
Outside of school and the MLH Fellowship, he works part-time as a finance & analytics 
manager at Sorare, a fantasy sports NFT platform, and enjoys outdoor activities and being a
plant dad (with a very black thumb).
""")

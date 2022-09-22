from ast import arg
import streamlit as st
import bentoml
from dynamic import stock_on_change, supported_stock, stock_name_format

# Interaction Part
st.markdown("# Interactions")

option = st.selectbox (
  'Which Stock would you like to learn more about?',
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



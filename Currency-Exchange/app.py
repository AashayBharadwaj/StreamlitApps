import streamlit as st
import pandas as pd
from data_manager import get_currency_options, get_historical_data

# Set up the page title and layout
st.title('Currency Exchange Rate Tracker')

# Load currency options
currency_options = get_currency_options()

# Default currency and period settings
from config import default_currency, default_period, time_periods

# UI for currency selection
currency = st.selectbox('Currency Pair', options=currency_options, index=currency_options.index(default_currency))

# UI for time period selection
selected_period = st.radio("Select Time Period", time_periods, index=time_periods.index(default_period), horizontal=True)

# Display the historical data chart
historical_data = get_historical_data(currency, selected_period)
if isinstance(historical_data, pd.DataFrame):
    st.write(f"Historical data for {currency} over {selected_period}:")
    st.line_chart(historical_data['Close'])
else:
    st.write(historical_data)

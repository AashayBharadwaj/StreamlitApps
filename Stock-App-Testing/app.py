import streamlit as st
from datetime import datetime
from functions.ui_elements import render_header_and_text
from functions.data_fetching import get_ticker_options, fetch_stock_data
from functions.data_processing import process_price_data, plot_dual_y_axes, calculate_annual_return, calculate_standard_deviation, calculate_risk_adjusted_return


# Default values
default_ticker = 'MSFT'
default_ticker_2 = 'No Selection'
default_start_date = datetime(2020, 1, 1)
default_end_date = datetime.today()


# Get ticker options
ticker_options = get_ticker_options()

# Call the cached function to render header and text
render_header_and_text()

# User inputs with default values
st.sidebar.header('Select your first stock')
ticker = st.sidebar.selectbox('Stock Ticker', options=ticker_options, index=ticker_options.index(default_ticker))
start_date = st.sidebar.date_input('Start Date', value=default_start_date)
end_date = st.sidebar.date_input('End Date', value=default_end_date)

st.sidebar.header('Select another stock if you want to make a comparison')
ticker_2 = st.sidebar.selectbox('Stock Ticker',options=ticker_options,index=ticker_options.index(default_ticker_2))


# # Fetch stock data
data = fetch_stock_data(ticker, start_date, end_date)


# Check if the second ticker is selected and fetch data if it is
if ticker_2 != 'No Selection':
    data_2 = fetch_stock_data(ticker_2, start_date, end_date)
    # Plot stock data with dual y-axes
    fig = plot_dual_y_axes(data, ticker, data_2, ticker_2)
else:
    # Plot stock data for the first ticker only
    fig = process_price_data(data, ticker)

# Display the plot
st.plotly_chart(fig)





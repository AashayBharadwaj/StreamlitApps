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

# Create a layout with three columns
col1, col2, col3 = st.columns([1, 2, 1])

# Place the image in the center column
with col2:
    st.image('logos/test.svg', width=300)

# Call the cached function to render header and text
render_header_and_text()


# Sidebar options
option = st.sidebar.radio('Select an Option', ['Track Stock Performance', 'Track Portfolio'])


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
    explanation = f'This is how {ticker} has performed against {ticker_2} in the selected time period!'
else:
    # Plot stock data for the first ticker only
    fig = process_price_data(data, ticker)
    explanation = f'This is how {ticker} has performed in the selected time period!'

# Display the plot
st.plotly_chart(fig)
st.subheader(explanation)


# Create tabs for different data views
pricing_data = st.tabs(["Price Data"])

# Create tabs for different data views
pricing_data, fundamental_data, news = st.tabs(["Price Data", "Fundamental Data", "Top 10 News articles"])

with pricing_data:
    st.write('Price Movement')
    data2 = data.copy()
    data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data2.dropna(inplace=True)
    st.write(data2)
    
    annual_return = calculate_annual_return(data2)
    
    stdev = calculate_standard_deviation(data2)
    
    risk_adj_return = calculate_risk_adjusted_return(annual_return, stdev)

    # # Round values to two decimal places
    annual_return_rounded = round(annual_return, 2)
    stdev_rounded = round(stdev, 2)
    risk_adj_return_rounded = round(risk_adj_return, 2)

    # # Display the rounded values
    st.write('Annual Return is ', annual_return_rounded, '%')
    # st.write('Standard Deviation is ', stdev_rounded, '%')
    st.write('Risk Adj Return is', risk_adj_return_rounded, '%')


with fundamental_data:
    st.write('This part is work in progress!!')
    
with news:
    st.write('So is this!! Go look at the beautiful charts above!')
   

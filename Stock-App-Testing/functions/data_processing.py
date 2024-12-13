import plotly.express as px
import numpy as np
from datetime import datetime
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from .data_fetching import fetch_stock_data
# from app import ticker,start_date,end_date




def process_price_data(data, ticker):
    fig = px.line(data, x=data.index, y=data['Adj Close'], title=ticker)
    fig.update_yaxes(title_text=f"{ticker} Price")
    return fig


# Default values
default_ticker = 'MSFT'
default_ticker_2 = 'No Selection'
default_start_date = datetime(2020, 1, 1)
default_end_date = datetime.today()


def calculate_annual_return(data):
    return data['% Change'].mean() * 252 * 100

def calculate_standard_deviation(data):
    return np.std(data['% Change']) * np.sqrt(252) * 100

def calculate_risk_adjusted_return(annual_return, stdev):
    return annual_return / stdev

# Function to create a plot with two y-axes
def plot_dual_y_axes(data1, ticker1, data2=None, ticker2=None):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces for the first ticker
    fig.add_trace(
        go.Scatter(x=data1.index, y=data1['Adj Close'], name=ticker1, line=dict(color='#615EFC')),
        secondary_y=False,
    )

    # Add traces for the second ticker, if provided
    if data2 is not None and ticker2 is not None:
        fig.add_trace(
            go.Scatter(x=data2.index, y=data2['Adj Close'], name=ticker2, line=dict(color='#ACD793')),
            secondary_y=True,
        )

    # Add figure title
    fig.update_layout(
        title_text="Stock Price Data"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Date")

    # Set y-axes titles with just the ticker name followed by "Price"
    fig.update_yaxes(title_text=f"{ticker1} Price", secondary_y=False)
    fig.update_yaxes(title_text=f"{ticker2} Price", secondary_y=True)

    return fig



# # # Fetch stock data
# data = fetch_stock_data(ticker, start_date, end_date)


def process_data_and_metrics(data):
    data2 = data.copy()
    data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data2.dropna(inplace=True)

    annual_return = calculate_annual_return(data2)
    stdev = calculate_standard_deviation(data2)
    risk_adj_return = calculate_risk_adjusted_return(annual_return, stdev)

    # Round values to two decimal places
    annual_return_rounded = round(annual_return, 2)
    stdev_rounded = round(stdev, 2)
    risk_adj_return_rounded = round(risk_adj_return, 2)

    # Display the rounded values
    st.write('Annual Return is ', annual_return_rounded, '%')
    st.write('Risk Adj Return is', risk_adj_return_rounded, '%')
    
    return data2, annual_return_rounded, stdev_rounded, risk_adj_return_rounded


    
    return data2, annual_return_rounded, stdev_rounded, risk_adj_return_rounded



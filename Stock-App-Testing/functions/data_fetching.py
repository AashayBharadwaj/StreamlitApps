import pandas as pd
import yfinance as yf

def get_ticker_options():
    ticker_data = pd.read_csv('../Stock-Tickers.csv')
    return ticker_data['Tickers'].tolist()

def fetch_stock_data(ticker, start_date, end_date):
    return yf.download(ticker, start=start_date, end=end_date)

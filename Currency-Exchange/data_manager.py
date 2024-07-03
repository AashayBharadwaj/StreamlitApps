
import pandas as pd
import yfinance as yf

def get_currency_options():
    currency_data = pd.read_csv('currencies.csv')
    return currency_data['currency'].tolist()

def get_historical_data(pair_code, period):
    try:
        yf_code = f"{pair_code}=X"
        data = yf.download(yf_code, period=period)
        if not data.empty:
            return data
        else:
            return "No data available"
    except Exception as e:
        return f"An error occurred: {e}"

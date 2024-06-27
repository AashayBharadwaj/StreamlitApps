import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
import os
from alpha_vantage.fundamentaldata import FundamentalData
from config import API_KEY
from stocknews import StockNews
from datetime import datetime



st.title('Stock Dahsboard')

# Default values
default_ticker = 'MSFT'
default_start_date = datetime(2020, 1, 1)
default_end_date = datetime.today()

# Read tickers from a CSV file
ticker_data = pd.read_csv('Stocks-Charting/Stock-Tickers.csv')
ticker_options = ticker_data['Tickers'].tolist()

# User inputs with default values
# ticker = st.sidebar.text_input('Ticker', value=default_ticker)
ticker = st.sidebar.selectbox('Ticker', options=ticker_options, index=ticker_options.index(default_ticker))
start_date = st.sidebar.date_input('Start Date', value=default_start_date)
end_date = st.sidebar.date_input('End Date', value=default_end_date)

data = yf.download(ticker,start=start_date, end=end_date)
fig = px.line(data, x=data.index, y=data['Adj Close'], title= ticker)
st.plotly_chart(fig)


pricing_data, fundamental_data, news = st.tabs(["Price Data", "Fundamental Data", "Top 10 News articles"])

with pricing_data:
    st.write('Price Movement')
    data2 = data
    data2['% Change'] = data['Adj Close']/data['Adj Close'].shift(1) -1 
    data2.dropna(inplace= True)
    st.write(data2)
    annual_return = data2['% Change'].mean()*252*100
    st.write('Annual Return is ', annual_return, '%')    
    stdev = np.std(data2['% Change'])*np.sqrt(252)
    st.write('Standard Deviation is ',stdev*100,'%')
    st.write('Risk Adj Return is', annual_return/(stdev*100))
    
# with fundamental_data:
#     key = API_KEY
#     fd=FundamentalData(key,output_format ='pandas')
#     st.subheader('Balance Sheet')
#     balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
#     bs = balance_sheet.T[2:]
#     bs.columns = list(balance_sheet.T.iloc[0])
#     st.write(bs)
    
#     st.subheader('Income Statement')
#     income_statement = fd.get_income_statement_annual(ticker)[0]
#     is1 = income_statement.T[2:]
#     is1.columns = list(income_statement.T.iloc[0])
#     st.write(is1)
    
#     st.subheader('Cash Flow Statement')
#     cash_flow = fd.get_cash_flow_annual(ticker)[0]
#     cf = cash_flow.T[2:]
#     cf.columns = list(cash_flow.T.iloc[0])
#     st.write(cf)
#     st.write('Fundamental')
    
# with news:
#     st.header(f'News of {ticker}')
#     sn = StockNews(ticker, save_news=False)
#     df_news = sn.read_rss()
#     for i in range(10):
#         st.subheader(f'News {i+1}')
#         st.write(df_news['published'][i])
#         st.write(df_news['title'][i])
#         st.write(df_news['summary'][i])
#         title_sentiment = df_news['sentiment_title'][i]
#         st.write(f'Title Sentiment {title_sentiment}')
#         news_sentiment = df_news['sentiment_summary'][i]
#         st.write(f'News Sentiment {news_sentiment}')
    

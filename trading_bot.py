import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
import plotly.express as px



def get_data(symbol,start,end):
    try:
        stock_df = yf.download(symbol,start=start,end=end)
    except:
        print(f"Error in fetching data from the exchange:{symbol}")
    return stock_df

data=yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

print(data)
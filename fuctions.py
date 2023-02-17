import plotly.graph_objects as go
import dash
import ccxt
import yfinance as yf
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import dcc
from dash import html
import pandas as pd
import numpy as np
from IPython.display import display
from dash.dependencies import Output, Input
import json
import matplotlib.pyplot as mp
import plotly.express as px
import datetime
import os
from binance.client import Client
import time
from time import sleep
import ccxt
import talib
import numpy as np
from datetime import datetime
import pandas as pd
from IPython.display import display




def dataframe_creation2(data, start, end):
    data["currency"] = "€"
    data["date"] = pd.to_datetime(data["date"]).dt.date
    data = data.where((data.date) >= (start))
    data = data.where((data.date) <= (end))
    data = data.dropna()
    df_debit = data.where(data.credit == 0)
    df_credit = data.where(data.credit != 0)
    df_debit = df_debit.dropna()
    df_credit = df_credit.dropna()
    df_credit = df_credit.reset_index()
    df_debit = df_debit.reset_index()
    df_credit['valeur'] = df_credit["credit"]
    df_debit['valeur'] = df_debit["debit"]
    del df_credit["index"]
    del df_credit["debit"]
    del df_debit["credit"]
    del df_debit["index"]
    df_credit['date'] = df_credit["date"]
    df_debit['date'] = df_debit["date"]
    categC = ("Salaire", "Virement", "Remboursement")
    categD = ("loyer", "abonnement", "course", "restauration", "divertissement", "shopping", "transport")
    return [df_credit, df_debit]

def dataframe_creation(data,start,end):
    data = data.where(data.date >= start)
    data = data.where(data.date <= end)
    data = data.dropna()
    data["currency"] = "€"
    data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d")
    df_debit = data.where(data.credit == 0)
    df_credit = data.where(data.debit == 0)
    df_debit = df_debit.dropna()
    df_credit = df_credit.dropna()
    df_credit = df_credit.reset_index()
    df_debit = df_debit.reset_index()
    del df_credit["index"]
    del df_debit["index"]

    categC = ("Salaire", "Virement", "remboursement")
    categD = ("loyer", "abonnement", "course", "restauration", "divertissement", "shopping", "transport")

    df_typeD = pd.DataFrame()
    df_typeD.at[0, "valeur"] = 0
    for j in range(len(categD)):
        s = 0
        for i in range(df_debit.shape[0]):
            if (df_debit.at[i, "type"] == categD[j]):
                s = s + df_debit.at[i, "debit"]

        df_typeD.at[j, "category"] = categD[j]
        df_typeD.at[j, "valeur"] = s
        df_typeD.at[j, "currency"] = '€'

    df_typeD = df_typeD.reset_index()
    del df_typeD["index"]

    df_typeC = pd.DataFrame()
    df_typeC.at[0, "valeur"] = 0
    for j in range(len(categC)):
        s = 0
        for i in range(df_credit.shape[0]):
            if (df_credit.at[i, "type"] == categC[j]):
                s = s + df_credit.at[i, "credit"]

        df_typeC.at[j, "category"] = categC[j]
        df_typeC.at[j, "valeur"] = s
        df_typeC.at[j, "currency"] = '€'
    df_typeC = df_typeC.reset_index()
    del df_typeC["index"]
    return [df_typeC, df_typeD]

def Total_dep_rev_sav(df_typeD,df_typeC):
    Total_depenses = sum(df_typeD.valeur)
    Total_revenues = sum(df_typeC.valeur)
    savings = Total_revenues - Total_depenses
    return[Total_depenses,Total_revenues,savings]

def evo_period(Total_depenses,Total_revenues,savings):
    df_eco = pd.DataFrame()
    df_eco.at[0, 'PERIOD'] = 'Aout1'
    df_eco.at[0, 'EXPENSES'] = Total_depenses

    df_eco['REVENUE'] = Total_revenues
    df_eco["SAVINGS"] = savings
    df_eco["REMAIN"] = 5000-savings
    return df_eco

def fucn_objectif(df_eco):
    new_data=[0,1]

    new_data[0]= df_eco.at[0,'SAVINGS']
    new_data[1]=5000
    return new_data

def titles_Totals(Total_depenses,Total_revenues):
    dep_t="total depenses = "+ str(Total_depenses)+"€"
    rev_t="total revenus = "+ str(Total_revenues)+"€"
    return [dep_t,rev_t]

def delai_obj(savings):
    delai=0
    dep_moy=2*savings
    i=0
    while((5000-i*dep_moy)>0):
        delai=delai+1
        i=i+1

    delai_t="le délai restant pour atteindre 5000€ = "+str(delai)+" mois"
    return delai_t
def total_calc(df):
    s=0
    for i in range(df.shape[0]):
        s=s+df.at[i,"valeur"]
    return s

def Home_total(test,T):
    df = pd.read_json(test, orient='split')
    df = df.dropna()
    d1 = datetime.date.today()
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df['month'] = pd.DatetimeIndex(df['date']).month
    df = df.where(df["month"] == d1.month)
    df = df.dropna()
    df = df.reset_index()
    del df["index"]
    tab1 = dataframe_creation(df,  df.at[0, "date"] ,  df.at[df.shape[0] - 1, "date"])
    tab0 = tab1[T].copy()
    Total_Inc_home = str(total_calc(tab0)) + " €"
    return [Total_Inc_home,total_calc(tab0)]
def Home_total_S(test,start,end):
    df = pd.read_json(test, orient='split')
    df = df.dropna()
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df = df.where(df.date >= start)
    df = df.where(df.date <= end)
    df = df.dropna()
    df = df.reset_index()
    del df["index"]
    tab1 = dataframe_creation(df,  df.at[0, "date"] ,  df.at[df.shape[0] - 1, "date"])
    tab_R = tab1[0].copy()
    total_rev=total_calc(tab_R)
    tab_E=tab1[1].copy()
    total_exp = total_calc(tab_E)
    sav=total_rev-total_exp
    return sav



#################### BOURSE     #######################

exchange = ccxt.binance()

# STEP 1: FETCH THE DATA
def fetch_data2(ticker):
    global exchange
    bars,ticker_df = None, None

    try:
        bars = exchange.fetch_ohlcv(ticker, timeframe=f'{CANDLE_DURATION_IN_MIN}m', limit=100)
    except:
        print(f"Error in fetching data from the exchange:{ticker}")

    if bars is not None:
        ticker_df = pd.DataFrame(bars[:-1], columns=['at', 'open', 'high', 'low', 'close', 'vol'])
        ticker_df['Date'] = pd.to_datetime(ticker_df['at'], unit='ms')
        ticker_df['symbol'] = ticker

    return ticker_df

def get_data(symbol,per):

        data = yf.Ticker(symbol).history(period=per)
        data = data.reset_index()
        data["Date"] = pd.to_datetime(data["Date"]).dt.date

        return data

def update_Trends(ticker_name,per):
        stock_df=get_data(ticker_name,per)
        if stock_df is not None:
            candlestick = go.Candlestick(x=stock_df.Date,
                                         open=stock_df['Open'],
                                         high=stock_df['High'],
                                         low=stock_df['Low'],
                                         close=stock_df['Close'])
            fig = go.Figure(data=[candlestick])
            fig.layout.xaxis.type = 'category'
            fig.layout.yaxis.title='value in USD ($)'
            return fig
        else:
            return "There's no symbol with this name"


def currency_pair(ticker1, ticker2):
    pair = str(ticker1 + '/' + ticker2)
    return pair

def fetch_cryptodata(ticker,tf):
    global exchange
    bars,ticker_df = None, None
    try:
        bars = exchange.fetch_ohlcv(ticker, timeframe=str(tf), limit=100) #faire varier timeframe
    except:
        print(f"Error in fetching data from the exchange:{ticker}")

    if bars is not None:
        ticker_df = pd.DataFrame(bars[:-1], columns=['at', 'open', 'high', 'low', 'close', 'vol'])
        ticker_df['Date'] = pd.to_datetime(ticker_df['at'], unit='ms')
        ticker_df['symbol'] = ticker

    return ticker_df

def fetch_data(ticker,tf):
    global exchange
    bars,ticker_df = None, None

    try:
        bars = exchange.fetch_ohlcv(ticker, timeframe=str(tf), limit=100) #faire varier timeframe
    except:
        print(f"Error in fetching data from the exchange:{ticker}")

    if bars is not None:
        ticker_df = pd.DataFrame(bars[:-1], columns=['at', 'open', 'high', 'low', 'close', 'vol'])
        ticker_df['Date'] = pd.to_datetime(ticker_df['at'], unit='ms')
        ticker_df['symbol'] = ticker

    return ticker_df


#################### BOT TRADING    #######################


exchange = ccxt.binance()

# STEP 1: FETCH THE DATA
def fetch_data2(ticker):
    global exchange
    bars,ticker_df = None, None

    try:
        bars = exchange.fetch_ohlcv(ticker, timeframe=f'1m', limit=100) #faire varier timeframe
    except:
        print(f"Error in fetching data from the exchange:{ticker}")

    if bars is not None:
        ticker_df = pd.DataFrame(bars[:-1], columns=['at', 'open', 'high', 'low', 'close', 'vol'])
        ticker_df['Date'] = pd.to_datetime(ticker_df['at'], unit='ms')
        ticker_df['symbol'] = ticker

    return ticker_df


def get_trade_recommendation(ticker_df):
    macd_result, final_result = 'WAIT', 'WAIT'
    RSI_OVERSOLD = 40
    RSI_OVERBOUGHT = 30

    # BUY or SELL based on MACD crossover points and the RSI value at that point
    macd, signal, hist = talib.MACD(ticker_df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    last_hist = hist.iloc[-1]
    prev_hist = hist.iloc[-2]
    if not np.isnan(prev_hist) and not np.isnan(last_hist):
        # If hist value has changed from negative to positive or vice versa, it indicates a crossover
        macd_crossover = (abs(last_hist + prev_hist)) != (abs(last_hist) + abs(prev_hist))
        if macd_crossover:
            macd_result = 'BUY' if last_hist > 0 else 'SELL'

    if macd_result != 'WAIT':
        rsi = talib.RSI(ticker_df['close'], timeperiod=14)
        last_rsi = rsi.iloc[-1]
        if (last_rsi <= RSI_OVERSOLD):
            final_result = 'BUY'
        elif (last_rsi >= RSI_OVERBOUGHT):
            final_result = 'SELL'

    return final_result


def execute_trade(trade_rec_type, trading_ticker):
    Binance_APIkey = 'YOUR_API_KEY'
    Binance_APIsecret = 'YOUR_API_SECRET'

    client = Client(Binance_APIkey, Binance_APIsecret)
    client.API_URL = 'https://testnet.binance.vision/api'
    ticker_price = client.get_symbol_ticker(symbol=trading_ticker)
    price = ticker_price["price"]
    order_placed = False
    order = client.create_order(symbol=trading_ticker, side=trade_rec_type, type='MARKET', quantity=1)
    orderId = order["orderId"]
    print('{} order placed at {}\n'.format(trade_rec_type, price))
    while True:
        currentOrder = client.get_order(symbol=trading_ticker, orderId=orderId)
        if currentOrder['status'] == 'FILLED':
            print("{}: {} {} at {}".format(trade_rec_type.lower(), 1, trading_ticker, price))
            order_placed = True
            break

    return order_placed

def run_bot_for_ticker(ccxt_ticker, trading_ticker,on,df):
    CANDLE_DURATION_IN_MIN=1
    currently_holding = False
    while on:
        # STEP 1: FETCH THE DATA
        ticker_data = fetch_data2(ccxt_ticker)
        if ticker_data is not None:
            # STEP 2: COMPUTE THE TECHNICAL INDICATORS & APPLY THE TRADING STRATEGY
            trade_rec_type = get_trade_recommendation(ticker_data)
            print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}  TRADING RECOMMENDATION: {trade_rec_type}')
            df['date']=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            df['Recommandation']=trade_rec_type
            # STEP 3: EXECUTE THE TRADE
            trade_rec_type='SELL'
            if (trade_rec_type == 'BUY' and not currently_holding) or \
                (trade_rec_type == 'SELL' and currently_holding):
                print(f'Placing {trade_rec_type} order')
                trade_successful = execute_trade(trade_rec_type,trading_ticker)
                currently_holding = not currently_holding if trade_successful else currently_holding

            # SLEEP BEFORE REPEATING THE STEPS
            time.sleep(CANDLE_DURATION_IN_MIN*60)
        else:
            print(f'Unable to fetch ticker data - {ccxt_ticker}. Retrying!!')
            time.sleep(5)

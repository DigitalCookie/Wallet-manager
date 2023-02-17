import ccxt
import dash_daq as daq

from fuctions import *
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

Style_Row2 = {'border': '1px lightgrey solid', 'border-radius': 5, 'padding': '10px', 'vertical-align': 'middle',
             'backgroundColor': '#C6EBC5',
             'margin-bottom': '10px', 'margin-left': '0px', 'margin-right': '0px', 'margin-top': '9px',
             'box-shadow': '1px 1px 2px ' + '#C6EBC5',
             'align-content': 'center'}


df = pd.read_excel("crypto_list.xlsx")
#df_cop=df_data[['High','Low','Open','Close']].copy()
layout=html.Div(children=[
    dbc.Container([
        dbc.Row([
            html.P(' .', style={'margin-bottom': '0.25em'}),

            dbc.Col([html.H1('CryptoMarket', style={'font-size': '350%',
                                                 'text-align': 'center',
                                                 'color':'#A1C298',
                                                 'font-weight': 'heavy',
                                                 'margin-top': '2em',
                                                 }),]),

        ],justify='center'),
        dbc.Row([html.Img(src="assets/cryptocurrency.png", style={"max-width": "7%",'margin-bottom': '1.5em','text-align':'center'})],justify='center') ,

        dbc.Row([
            dbc.Col([
                html.P("Base Currency  ", style={
                    'font-size': '100%',
                    'font': 'Copperplate',
                    'text-align': 'left',
                    'margin-left': '0.5em',
                    'color': ' #A1C298',  # A1C298
                    'font-weight': 'lighter', }),
            ],width='auto'),
            dbc.Col([
                dcc.Dropdown(   id="crypto-dropdown",
                                options = [{"label": row["Name"], "value": row["Symbol"]} for index, row in df.iterrows()],
                                value = 'BTC',
                                placeholder = "Select a currency",
                                style={"width":"200px"}

                )
            ],width='auto'),
            dbc.Col([
                            html.P("Quote Currency  ", style={
                                'font-size': '100%',
                                'font': 'Copperplate',
                                'text-align': 'left',
                                'margin-left': '0.5em',
                                'color': ' #A1C298',  # A1C298
                                'font-weight': 'lighter', }),
                        ],width='auto'),
                        dbc.Col([
                            dcc.Dropdown(   id="crypto2-dropdown",
                                            options = [{"label": 'USDT', "value":'USDT'},
                                                       {"label": 'EUR', "value":'EUR'}],
                                            value = 'USDT',
                                            placeholder = "Select a name",
                                            style={"width":"200px"}

                            )
                        ],width='auto'),
            dbc.Col([
                html.P("Timeframe   ", style={
                    'font-size': '100%',
                    'font': 'Copperplate',
                    'text-align': 'left',
                    'margin-left': '0.5em',
                    'color': ' #A1C298',  # A1C298
                    'font-weight': 'lighter', }),
            ],width='auto'),

            dbc.Col([
                dcc.Dropdown(id="tf-dropdown",
                            options=[
                                    {'label': '1m', 'value': '5m'},
                                    {'label': '5m', 'value': '5m'},
                                    {'label': "10m", 'value': "10m"},
                                    {'label': "15m", 'value': "15m"},
                                    {'label': '1h', 'value': '1h'},
                                    {'label': "3h", 'value': "3h"},
                                    {'label': '12h', 'value': '12h'},
                                    {'label': "1j", 'value': "1d"},
                                    {'label': "1M", 'value': "1M"},



                            ],
                            value='15m',
                            placeholder="Select timeframe",

                             )
            ],width='auto'),
        ], justify='left', className="p-3 border bg-light" ),
        dbc.Row([
            dbc.Col([
                dcc.Loading(html.Div(id='out_put_Cr'),color='#FB4570',type='cube')
            ])
        ],style=Style_Row2),
        dbc.Row([
                    html.P(' .', style={'margin-bottom': '0.25em'}),

                    dbc.Col([html.H1('Trading Bot', style={'font-size': '350%',
                                                         'text-align': 'center',
                                                         'color':'#A1C298',
                                                         'font-weight': 'heavy',
                                                         'margin-top': '2em',
                                                         }),]),

        ],justify='center'),
        dbc.Row([html.Img(src="assets/robot.png", style={"max-width": "7%",'margin-bottom': '1.5em','text-align':'center'})],justify='center') ,
        daq.BooleanSwitch(id='c-switch',
                          label='ON / OFF',
                          color="#9B51E0",
                          on=False,
                          theme='plotly_dark',
                          style={'backgroud-color':'red'},
                          labelPosition='bottom'),
        dbc.Row([
            dbc.Col([
                html.Div(id='c-switch-output-1')
            ])
        ]),


                html.P(' .',style={'margin-top':'5em','margin-bottom':'5em'})
    ],style={'margin-top':'3em','align':'center','max-width': '100%','height':'auto','background-color':'#FBF2CF','margin-bottom':'0em','opacity':'0.75'})
])
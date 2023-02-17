import ccxt

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


df = pd.read_csv("nasdaq_screener_1672928102560.csv")
#df_cop=df_data[['High','Low','Open','Close']].copy()
layout=html.Div(children=[
    dbc.Container([
        dbc.Row([
            html.P(' .', style={'margin-bottom': '0.25em'}),

            dbc.Col([html.H1('Bourse', style={'font-size': '350%',
                                                 'text-align': 'center',
                                                 'color':'#A1C298',
                                                 'font-weight': 'heavy',
                                                 'margin-top': '2em',
                                                 }),]),

        ],justify='center'),
        dbc.Row([html.Img(src="assets/trends2.png", style={"max-width": "7%",'margin-bottom': '1.5em','text-align':'center'})],justify='center') ,

        dbc.Row([
            dbc.Col([
                html.P("Stock Exchange   ", style={
                    'font-size': '100%',
                    'font': 'Copperplate',
                    'text-align': 'left',
                    'margin-left': '0.5em',
                    'color': ' #A1C298',  # A1C298
                    'font-weight': 'lighter', }),
            ], width='auto'),
            dbc.Col([
                dcc.Dropdown(id="se-dropdown",
                             options=[{'label': 'NYSE', 'value': 'NYSE'},
                                      {'label': 'EURONEXT', 'value': 'EURONEXT'},],
                             value='NYSE',
                             placeholder="Select a stock exchange",
                             style={"width": "200px"}

                             )
            ], width='auto'),
            dbc.Col([
                html.P("Stock Name   ", style={
                    'font-size': '100%',
                    'font': 'Copperplate',
                    'text-align': 'left',
                    'margin-left': '0.5em',
                    'color': ' #A1C298',  # A1C298
                    'font-weight': 'lighter', }),
            ],width='auto'),
            dbc.Col([
                dcc.Dropdown(   id="name-dropdown",
                                options = [{"label": row["Name"], "value": row["Name"]} for index, row in df.iterrows()],
                                value = None,
                                placeholder = "Select a name",
                                style={"width":"500px"}

                )
            ],width='auto'),
            dbc.Col([
                html.P("Period   ", style={
                    'font-size': '100%',
                    'font': 'Copperplate',
                    'text-align': 'left',
                    'margin-left': '0.5em',
                    'color': ' #A1C298',  # A1C298
                    'font-weight': 'lighter', }),
            ],width='auto'),
            #1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            dbc.Col([
                dcc.Dropdown(id="period-dropdown",
                            options=[ {'label': 'Année courante', 'value': 'ytd'},
                                      {'label': '1 jour', 'value': '1d'},
                                      {'label': "1 mois", 'value': "1mo"},
                                      {'label': '3 mois', 'value': '3mo'},
                                      {'label': '6 mois', 'value': '6mo'},
                                      {'label': '1 an', 'value': '1y'},
                                      {'label': '5 ans', 'value': '5y'},
                                      {'label': '10 ans', 'value': '10y'},
                                      {'label': 'max', 'value': 'max'},


                            ],
                            value='ytd',
                            placeholder="Select period",

                             )
            ],width='auto'),
        ], justify='left', className="p-3 border bg-light" ),
        dbc.Row([
            dbc.Col([
                dcc.Loading(html.Div(id='out_put_B'),color='#FB4570',type='cube')
            ])
        ],style=Style_Row2),

                html.P(' .',style={'margin-top':'5em','margin-bottom':'5em'})
    ],style={'margin-top':'3em','align':'center','max-width': '100%','height':'auto','background-color':'#FBF2CF','margin-bottom':'0em','opacity':'0.75'})
])
''' dbc.Row([
            dbc.Col([
                dcc.Loading(dcc.Graph(id='Bar_Chart_B'),color='#501B1D',type='cube')
            ])
        ],style=Style_Row2),''',


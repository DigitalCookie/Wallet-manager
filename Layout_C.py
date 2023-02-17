
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


df_data = pd.read_excel("Budget.xlsx", sheet_name="Suivi budget")
#df_cop=df_data[['High','Low','Open','Close']].copy()
layout=html.Div(children=[
    dbc.Container([
        dbc.Row([
            html.P(' .', style={'margin-bottom': '0.25em'}),

            dbc.Col([html.H1('Income', style={'font-size': '350%',
                                                 'text-align': 'center',
                                                 'color':'#A1C298',
                                                 'font-weight': 'heavy',
                                                 'margin-top': '2em',
                                                 }),]),

        ],justify='center'),
       dbc.Row([html.Img(src="assets/income.png", style={"max-width": "10%",'margin-bottom': '1.5em','text-align':'center'})],justify='center') ,
        dbc.Row([
                    dbc.Col([
                        dcc.DatePickerRange(
                            id='date-pick-C',
                            min_date_allowed=df_data.date.min(),
                            max_date_allowed=df_data.date.max(),
                            start_date=df_data.date.min(),
                            end_date=df_data.date.max(),
                            style={'backgroud-color':'#501B1D','border-color':'#501B1D'},


                            )
                         ]),
                ]),
        dbc.Row([
            dbc.Col([
                dcc.Loading(dcc.Graph(id='Bar_Chart_C'),color='#501B1D',type='cube')
            ])
        ],style=Style_Row2),
        dbc.Row([
            dbc.Col([
                dcc.Loading(dcc.Graph(id='Pie_Chart_C'), color='#501B1D', type='cube')
            ])
        ],style=Style_Row2),
                html.P(' .',style={'margin-top':'5em','margin-bottom':'5em'})
    ],style={'margin-top':'3em','align':'center','max-width': '100%','height':'auto','background-color':'#FBF2CF','margin-bottom':'0em','opacity':'0.75'})
])


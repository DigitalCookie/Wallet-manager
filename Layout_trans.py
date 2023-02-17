
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

            dbc.Col([html.H1('Transactions ', style={'font-size': '350%',
                                                 'text-align': 'center',
                                                 'color':'#A1C298',
                                                 'font-weight': 'heavy',
                                                 'margin-top': '2em',
                                                 }),]),

        ],justify='center'),
        dbc.Row([

            dbc.Col([ dbc.Button(children='Ajouter une transacation', id='add_trans',color= "danger",name='Hide Summary',outline=True,size="lg"), ]),

        ], justify='center',align='center', style={'margin-bottom':'3em'}),
        dbc.Row([html.Div(id='Formulaire')], style={"background-color": '#FA7070'}),

                html.P(' .',style={'margin-top':'30em','margin-bottom':'5em'})
    ],style={'margin-top':'3em','align':'center','max-width': '100%','height':'auto','background-color':'#FBF2CF','margin-bottom':'0em','opacity':'0.75'})
])


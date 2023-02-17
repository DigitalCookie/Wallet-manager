
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




layout=html.Div(children=[

    dbc.Container([
        dbc.Row([
            html.P(' .',style={'margin-bottom':'0.25em'}),
            html.H1('Wallet Manager',style={'font-size':'500%',
                                            'font':'Copperplate',
                                        'text-align':'center',
                                        'color':'#A1C298',
                                        'font-weight': 'lighter',
                                        'margin-top': '1em',
                                        'margin-bottom': '0.5em'}),
        ],justify="center"),
        dbc.Row([
            dbc.Col([
                html.P('Bienvenue dans Wallet Manager. Visualisez vos dépenses, vos revenus et votre épragne en toute simplicité. ', style={'font-size':'120%','width':'100%','font-weight': 'lighter', 'text-align':'center','font-style': 'italic','color':'#A1C298'})
            ] ,width=6,style={'backgroud-color':'rgba(0,0,0,0.45)','padding':'5px','align':'center'})
        ],style={'backgroud-color':'rgba(0,0,0,0.45)','padding':'5px','align':'center',},justify="center"),
        dbc.Row([
            html.Img(src="assets/wallet.png",style={"max-width":"20%"})
        ],justify="center"),
        dbc.Row([
            dbc.Col([
                dbc.Button(children='Show Summary', id='afficher-Button',color= "danger",name='Hide Summary',outline=True,size="lg"),
                #html.Button('Submit', id='afficher-Button', n_clicks=0),
            ],width='auto')
        ],justify='center',style={'margin-top':'5em'}),
        #dbc.Row([html.Div(id='output-button',children=[html.P("test")])],style={"background-color":'black'}),
        dbc.Row([
                dbc.Col([
                            html.Div(id='Expenses-Home'),
                ],style={'background-color':'#A1C298'}),

                dbc.Col([
                            html.Div(id='Income-Home'),
                ]),

             ],style={'background-color': '#C6EBC5','margin-top':'4em'}),
        dbc.Row([html.Div(id='cashflow')],style={"background-color":'#FA7070'}),

        html.P(' .',style={'margin-top':'5em','margin-bottom':'5em'}),


    ],style={'margin-top':'3em','align':'center','max-width': '100%','height':'auto','background-color':'#FBF2CF','margin-bottom':'0em','opacity':'0.75'})
    ])


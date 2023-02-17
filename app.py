#!/usr/bin/env python
# coding: utf-8

# In[105]:


import dash
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
from dash import dash_table
from fuctions import *
from dash import Dash, html, dcc,ctx
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
import plotly.graph_objects as go
import matplotlib.pyplot as mp
import plotly.express as px
import datetime
from datetime import datetime
import  Layout_home,Layout_D,Layout_C,Layout_trans,Layout_savings,Layout_bourse,Layout_crypto


pd.options.plotting.backend = "plotly"
pd.set_option('display.max_columns', 1000)  # or 1000.
pd.set_option('display.max_rows', 1000)  # or 1000.
pd.set_option('display.max_colwidth', 199)  # or 199.
pd.set_option('display.float_format', lambda x: '%0.2f' % x)

Style_Row = {'border': '1px lightgrey solid', 'border-radius': 5, 'padding': '10px', 'vertical-align': 'middle',
             'backgroundColor': 'rgba(0,0,0,0.85)',
             'margin-bottom': '10px', 'margin-left': '0px', 'margin-right': '0px', 'margin-top': '9px',
             'box-shadow': '1px 1px 2px ' + 'rgba(0,0,0,0.85)',
             'align-content': 'center'}
# In[106]:


app = Dash(__name__,
           suppress_callback_exceptions=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title = "Manage Your Wallet"

bottom_bar = html.Div('© Copyright - Nassime MEZIANE',
                      style={'font-style': 'italic', 'background-color': 'black', 'bottom': '0', 'position': 'fixed',
                             'color': 'white', 'width': '100%', 'padding': '5px', 'font-size': '8px',

                             'margin-top': '20px','align':'center'})

global data1

data1 = pd.read_excel("Budget.xlsx", sheet_name="Suivi budget")
app.layout = html.Div([
    dcc.Store(id='memory'),
    dcc.Location(id="url"),
    dbc.Navbar(dbc.Container([
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src='assets/wallet_image.png', height="30px"), ),
                    dbc.Col([dbc.NavbarBrand("Wallet Manager", className="ms-2", href="/")],style={"textDecoration": "red"},),

                    dbc.Col(
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem("Evolution de l'épargne", href="/epargne"),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="Epargne",
                            color='white',
                            # size='lg',
                            align_end=False,
                            toggle_style={
                                #"textTransform": "uppercase",
                                #"background": "#FB79B3",
                                "color":"white"},
                            style={'text': 'white','color': 'white'}
                        )
                    ),
                    dbc.Col(
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem("Ajouter Transaction", href="/trans"),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="Transactions",
                            color='white',
                            # size='lg',
                            align_end=False,
                            toggle_style={
                                #"textTransform": "uppercase",
                                #"background": "#FB79B3",
                                "color":"white"},
                            style={'text': 'white','color': 'white'}
                        )
                    ),
                    dbc.Col(
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem("Visualisation des dépenses ", href="/dep"),
                                dbc.DropdownMenuItem("Visualisation de revenues ", href="/rev")
                            ],
                            nav=True,
                            in_navbar=True,
                            label="Dépenses & Revenues",
                            color='white',
                            # size='lg',
                            align_end=False,
                            toggle_style={
                                #"textTransform": "uppercase",
                                #"background": "#FB79B3",
                                "color":"white"},
                            style={'text': 'white','color': 'white'}
                        )
                    ),
                    dbc.Col(
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem("Bourse", href="/trends"),
                                dbc.DropdownMenuItem("Crypto Exchange", href="/crypto"),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="Investissement",
                            color='white',
                            # size='lg',
                            align_end=False,
                            toggle_style={
                                #"textTransform": "uppercase",
                                #"background": "#FB79B3",
                                "color":"white"},
                            style={'text': 'white','color': 'white'}
                        )
                    ),
                ],
                align="center",
                className="g-0",
            ),
            # href="/",
            style={"textDecoration": "none"},
        ),
    ], style={
        "max-width": "none", "align": "center"  # , "vertical-align": "top", "padding": "0", 'top': '0'
    }), color="#FA7070", dark=True, light=True, sticky='top',
        style={'position': 'absolute', 'top': '0', 'width': '100vw', 'left': '0', 'right': '0'}),
    html.Div(id='page_affiche'),
    bottom_bar,

])

@app.callback(Output("page_affiche", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return Layout_home.layout
    elif pathname == "/dep":
        return Layout_D.layout
    elif pathname == "/rev":
        return Layout_C.layout  # Layout_R
    elif pathname == "/trans":
        return Layout_trans.layout
    elif pathname == "/epargne":
        return Layout_savings.layout
    elif pathname == "/trends":
        return Layout_bourse.layout
    elif pathname == "/crypto":
        return Layout_crypto.layout
    else:
        return html.P("test1")

    # If the user tries to reach a different page, return a 404 message



'''@app.callback(
    Output('graph_BTC', 'figure'),
    Input('date-pick', 'start_date'),
    Input('date-pick', 'end_date'),
    Input('dropdown-1', 'value'))
def update_graph_BTC(start_date, end_date,choix):
    df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/IAM.PA?period1=1102896000&period2=1664928000&interval=1d&events=history&includeAdjustedClose=true')
    df2=df.where(df.Date>=start_date)
    df3=df2.where(df.Date<=end_date)
    df3=df3.dropna()
    fig = px.line(df3,
                  x='Date',
                  y=choix,
                  template='plotly_dark'
                  )
    return fig
'''

#################################### DATA #########################################
@app.callback(Output('memory', 'data'),
              Input('memory', 'data'))
def update_data(fic_excel):
    if fic_excel is None:
        df=pd.read_excel("Budget.xlsx", sheet_name="Suivi budget")
        return  df.to_json(orient="split")
    else:
        df = pd.read_excel("Budget.xlsx", sheet_name="Suivi budget")
        return df.to_json(orient="split")




#################################### HOME PAGE ########################################

@app.callback(
     Output('afficher-Button',"active"),
     Input('afficher-Button', "children"))
def update_Summary_button(text):
        if(text=='Show Summary'):
            return False
        else:
            return True

@app.callback(
    Output('afficher-Button', "children"),
    Input('afficher-Button', "n_clicks"),
    Input('afficher-Button', "children")
)
def displayClick(click,text):
    if click is None:
        return "Show Summary"
    else:
        if "afficher-Button" == ctx.triggered_id:
            if(text=='Show Summary'):
                return "Hide Summary"
            elif(text=='Hide Summary'):
                return "Show Summary"

@app.callback(
    Output(component_id='Income-Home',  component_property='children'), #component_id='my-output', component_property='children'
    [
    Input(component_id='memory', component_property= 'data' ),
    Input('afficher-Button', "children")
     ]
)
def update_Inc_Home(fic,text):
    if(text == 'Hide Summary'):
        Total_Inc_home=Home_total(fic,0)
        children=[
            html.H1("Revenus ce mois ", style={
                        'font-size': '300%',
                        'font': 'Copperplate',
                        'text-align': 'center',
                        'color': ' #A1C298',  # A1C298
                        'font-weight': 'lighter', }),
                html.H1(Total_Inc_home[0],style={
                                                'font-size':'400%',
                                                'font':'Copperplate',
                                                'text-align':'center',
                                                'color':'blue', #A1C298
                                                'opacity':'0.8',
                                                'font-weight': 'lighter',})
                  ]
        return children
    elif(fic is None):

        return [html.H1("No Data", style={
            'font-size': '400%',
            'font': 'Copperplate',
            'text-align': 'center',
            'color': 'red',  # A1C298
            'font-weight': 'heavy', })]


@app.callback(
    Output('Expenses-Home', 'children'),
    Input('memory', "data"),
    Input('afficher-Button', "children")
)
def update_Exp_Home(fic,text):
    if (text == 'Hide Summary'):
        Total_exp_home=Home_total(fic,1)
        children=[html.H1("Dépenses ce mois ", style={
            'font-size': '300%',
            'font': 'Copperplate',
            'text-align': 'center',
            'color': ' #C6EBC5',  # A1C298
            'font-weight': 'lighter', }),
         html.H1(Total_exp_home[0], style={
             'font-size': '400%',
             'font': 'Copperplate',
             'text-align': 'center',
             'opacity': '0.8',
             'color': 'red',  # A1C298
             #"text-shadow": "2px 2px black",
             'font-weight': 'lighter', })]
        return children
    elif (fic is None):
        return [html.H1("No Data", style={
            'font-size': '400%',
            'font': 'Copperplate',
            'text-align': 'center',
            'color': 'red',  # A1C298
            'font-weight': 'heavy', })]

@app.callback(
    Output('cashflow', 'children'),
    Input('memory', "data"),
    Input('afficher-Button', "children"))
def update_Cashflow_Home(fic,text):
    if (text=='Hide Summary'):
        Rev=Home_total(fic, 0)
        Dep=Home_total(fic, 1)
        Cashflow=Rev[1]-Dep[1]
        children=[html.H1("Votre cashflow de ce mois-ci ", style={
            'font-size': '300%',
            'font': 'Copperplate',
            'text-align': 'center',
            'color': ' #FBF2CF',  # A1C298
            'font-weight': 'lighter', }),
         html.H1(str(Cashflow)+" €", style={
             'font-size': '400%',
             'font': 'Copperplate',
             'text-align': 'center',
             'opacity': '0.8',
             'color': '#C6EBC5',  # A1C298
             #"text-shadow": "2px 2px black",
             'font-weight': 'lighter', })]
        return children
    elif (fic is None):
        return [html.H1("No Data", style={
            'font-size': '400%',
            'font': 'Copperplate',
            'text-align': 'center',
            'color': 'red',  # A1C298
            'font-weight': 'heavy', })]





########################################## EXPENSES ##########################################

@app.callback(
    Output('Pie_Chart_D', 'figure'),
    Input('date-pick-D', 'start_date'),
    Input('date-pick-D', 'end_date'))
def update_Pie_Chart_D(start_date, end_date):
    df = pd.read_excel("Budget.xlsx", sheet_name="Suivi budget")
    df["date"] = pd.to_datetime(df["date"]).dt.date
    start_date = start_date[0:10]
    end_date = end_date[0:10]
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    df2 = df.where(df.date >= start_date)
    df3 = df2.where(df2.date <= end_date)
    tab1 = dataframe_creation(df3,start_date,end_date)
    tab0 = tab1[1].copy()
    titre="Total dépenses : "+str(total_calc(tab0))+" €"
    figure = px.pie(tab0,names='category', values='valeur',hole=.4,template='seaborn',title=titre)
    return figure
@app.callback(
    Output('Bar_Chart_D', 'figure'),
    Input('date-pick-D', 'start_date'),
    Input('date-pick-D', 'end_date'))
def update_Bar_Chart_D(start_date, end_date):
    df = pd.read_excel("Budget.xlsx", sheet_name="Suivi budget")
    start_date=start_date[0:10]
    end_date = end_date[0:10]
    start_date=datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date=datetime.strptime(end_date, "%Y-%m-%d").date()
    tab1 = dataframe_creation2(df,start_date,end_date)
    tab0=tab1[1].copy()
    figure = px.bar(tab0, x="date", y="valeur" , color='type',template='seaborn',text="name")
    return figure


########################################## INCOME ##########################################
@app.callback(
    Output('Bar_Chart_C', 'figure'),
    Input('date-pick-C', 'start_date'),
    Input('date-pick-C', 'end_date'))
def update_Bar_Chart_C(start_date, end_date):
    df = pd.read_excel("Budget.xlsx", sheet_name="Suivi budget")
    start_date=start_date[0:10]
    end_date = end_date[0:10]
    start_date=datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date=datetime.strptime(end_date, "%Y-%m-%d").date()
    tab1 = dataframe_creation2(df,start_date,end_date)
    tab0=tab1[0].copy()
    figure = px.bar(tab0, x="date", y="valeur" , color='type',template='seaborn',text="name")
    return figure

@app.callback(
    Output('Pie_Chart_C', 'figure'),
    Input('date-pick-C', 'start_date'),
    Input('date-pick-C', 'end_date'))
def update_Pie_Chart_C(start_date, end_date):
    df = pd.read_excel("Budget.xlsx", sheet_name="Suivi budget")
    df["date"] = pd.to_datetime(df["date"]).dt.date
    start_date = start_date[0:10]
    end_date = end_date[0:10]
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    df2 = df.where(df.date >= start_date)
    df3 = df2.where(df2.date <= end_date)
    tab1 = dataframe_creation(df3,start_date,end_date)
    tab0 = tab1[0].copy()
    titre="Total revenus : "+str(total_calc(tab0))+" €"
    figure = px.pie(tab0,names='category', values='valeur',hole=.4,template='seaborn',title=titre)
    return figure

########################################## TRANSACTIONS ##########################################
@app.callback(
     Output('add_trans',"active"),
     Input('add_trans', "children"))
def update_Summary_button(text):
        if(text=='Ajouter une transacation'):
            return False
        else:
            return True

@app.callback(
    Output('add_trans', "children"),
    Input('add_trans', "n_clicks"),
    Input('add_trans', "children")
)
def displayClick(click,text):
    if click is None:
        return "Ajouter une transacation"
    else:
        if "add_trans" == ctx.triggered_id:
            if(text=='Ajouter une transacation'):
                return "Remplissez le formulaire"
            elif(text=='Remplissez le formulaire'):
                return "Remplissez le formulaire"

@app.callback(
    Output(component_id='Formulaire',  component_property='children'), #component_id='my-output', component_property='children'
    [
    Input(component_id='memory', component_property= 'data' ),
    Input('add_trans', "children")
     ]
)
def update_trans(fic,text):
    choix1=["Dépense","Revenu"]
    categC = ["Salaire", "Virement", "remboursement"]
    categD = ["loyer", "abonnement", "course", "restauration", "divertissement", "shopping", "transport"]

    if(text == 'Remplissez le formulaire'):
        children=[
            dbc.Row([
                dbc.Col([
                    html.P("Date :", style={
                                'font-size': '200%',
                                'font': 'Copperplate',
                                'text-align': 'left',
                                'margin-left':'2em',
                                'color': ' #A1C298',  # A1C298
                                'font-weight': 'lighter', }),
                ]),
                dbc.Col([
                    dbc.Input(id="input-date", placeholder="Type something...", type="date",style={'margin-top':'10px','width': '270px'})
                ])
            ],justify='left',className="p-3 border bg-light",),
            dbc.Row([
                dbc.Col([
                    html.P("Nom : ", style={
                        'font-size': '200%',
                        'font': 'Copperplate',
                        'text-align': 'left',
                        'margin-left': '2em',
                        'color': ' #A1C298',  # A1C298
                        'font-weight': 'lighter', }),
                ]),
                dbc.Col([
                    dbc.Input(id="input-name", placeholder="Type something...", type="text",
                              style={'margin-top': '10px','width': '470px'})
                ])
            ], justify='left', className="p-3 border bg-light", ),
            dbc.Row([
                dbc.Col([
                    html.P("Type de Transaction :  ", style={
                        'font-size': '200%',
                        'font': 'Copperplate',
                        'text-align': 'left',
                        'margin-left': '2em',
                        'color': ' #A1C298',  # A1C298
                        'font-weight': 'lighter', }),
                ]),
                dbc.Col([
                    dcc.Dropdown(
                        choix1, id='dropdown_type_trans', value='choisir une valeur...',
                        multi=False,
                        style={'color': '#501B1D', 'width': '370px','margin-top': '10px'}
                    )
                ])
            ], justify='left', className="p-3 border bg-light", ),
            dbc.Row([
                dbc.Col([
                    html.P("Montant :  ", style={
                        'font-size': '200%',
                        'font': 'Copperplate',
                        'text-align': 'left',
                        'margin-left': '2em',
                        'color': ' #A1C298',  # A1C298
                        'font-weight': 'lighter', }),
                ]),
                dbc.Col([
                    dbc.Input(id="input-name", placeholder="Type value...", type="text",
                              style={'margin-top': '10px', 'width': '470px'})
                ])
            ], justify='left', className="p-3 border bg-light", ),
            dbc.Row([
                dbc.Col([
                    html.P("Catégorie de transaction :  ", style={
                        'font-size': '200%',
                        'font': 'Copperplate',
                        'text-align': 'left',
                        'margin-left': '2em',
                        'color': ' #A1C298',  # A1C298
                        'font-weight': 'lighter', }),
                ]),
                dbc.Col([
                    dbc.Input(id="input-name", placeholder="Type something...", type="text",
                              style={'margin-top': '10px', 'width': '470px'})
                ])
            ], justify='left', className="p-3 border bg-light", ),
            dbc.Row([

                dbc.Col([dbc.Button(children='Enregistrer transacation', id='save_trans', color="success",
                                    name='Enregister', outline=True, size="lg"), ], align='right'),

            ], justify='center', align='right', style={'margin-top': '3em','background-color':'#FBF2CF'}),

        ]
        return children
    elif(fic is None):

        return [html.H1("No Data", style={
            'font-size': '400%',
            'font': 'Copperplate',
            'text-align': 'center',
            'color': 'red',  # A1C298
            'font-weight': 'heavy', })]

########################################## SAVINGS ##########################################



@app.callback(
    Output('Bar_Chart_S', 'figure'),
    Input('memory', "data"),
    Input('date-pick-S', 'start_date'),
    Input('date-pick-S', 'end_date'))
def update_Bar_Chart_S(fic,start_date, end_date):
    val_S=Home_total_S(fic,start_date, end_date)
    tab0=pd.DataFrame()
    tab0.at[0,'period']=str(start_date)+' to '+str(end_date)
    tab0.at[0,'Cashflow']=val_S
    if (val_S<0):
        tab0.at[0,'type']='red'
    else:
        tab0.at[0,'type']='green'


    figure = px.bar(tab0, x="period", y="Cashflow", color='type', template='seaborn')

    return figure

########################################## Bourse ##########################################

list_tck = pd.read_csv("nasdaq_screener_1672928102560.csv")
new_list_tck=pd.DataFrame()
new_list_tck[["label","value"]]=list_tck[["Name","Symbol"]].copy()
options=new_list_tck.to_dict()


@app.callback(
    Output('name-dropdown', 'options'),
    Input('se-dropdown','value'),
)

def choix_tickers(choix_options):
    if (choix_options == 'NYSE'):
        list_tck = pd.read_csv("nasdaq_screener_1672928102560.csv")
    elif (choix_options == 'EURONEXT'):
        list_tck =  pd.read_excel("Euronext_Equities_2023-01-09.xlsx")
    list_tck=list_tck.dropna()

    options=[{"label": row["Name"], "value": row["Name"]} for index, row in list_tck.iterrows()]
    return options


@app.callback(
    Output('out_put_B', 'children'),
    Input('name-dropdown','value'),
    Input('period-dropdown','value'),
    Input('se-dropdown','value'),

)

def update_courbe(ticker_name,per,se):

    if ticker_name is not None :
        if (se=='NYSE'):
            list_tck = pd.read_csv("nasdaq_screener_1672928102560.csv")
        elif(se=='EURONEXT'):
            list_tck =  pd.read_excel("Euronext_Equities_2023-01-09.xlsx")
        used_t=list_tck.where(list_tck.Name==ticker_name)
        used_t = used_t.dropna()
        used_t = used_t.reset_index()
        del used_t['index']
        fig=update_Trends(used_t.Symbol[0],per)
        return [dcc.Graph(figure=fig)]
    else:
        return [html.P("enter something bro")]

########################################## Crypto ##########################################


@app.callback(
    Output('out_put_Cr', 'children'),
    Input('crypto-dropdown','value'),
    Input('crypto2-dropdown','value'),
    Input('tf-dropdown','value'),

)

def update_courbe(cr1,cr2,tf):

    if (cr1 and cr2 and tf) is not None :
       pair=currency_pair(cr1,cr2)
       df_crypto=fetch_data(pair,tf)
       candlestick = go.Candlestick(x=df_crypto['Date'],
                                    open=df_crypto['open'],
                                    high=df_crypto['high'],
                                    low=df_crypto['low'],
                                    close=df_crypto['close'])
       fig = go.Figure(data=[candlestick])
       #fig.layout.xaxis.type = 'category'
       fig.update_layout(template='plotly_dark')
       fig.layout.yaxis.title = str(cr1) +' value in ' + str(cr2)
       return [dcc.Graph(figure=fig)]

    else:
        return [html.P("enter something bro")]


@app.callback(
    Output('c-switch-output-1', 'children'),
    Input('c-switch', 'on')
)
def update_output(on):
    df_crypto_bot=pd.DataFrame()
    run_bot_for_ticker('ETH/USDT','ETHUSDT',on,df_crypto_bot)
    while on:
        return [html.P("the bot is running")]
    if df_crypto_bot is not None:
        return [dash_table.DataTable(df_crypto_bot.to_dict('records'), [{"name": i, "id": i} for i in df_crypto_bot.columns])]


if __name__ == '__main__':
    app.run_server(debug=True)

# In[ ]:


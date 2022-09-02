from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import plotly.express as px
from plotly.graph_objs import Line
from plotly.graph_objs.scatter.marker import Line
import dash_bootstrap_components as dbc

import line_chart
from line_chart import line_graf

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

metro_logo = 'https://cis.mosmetro.ru/strapi/uploads/MM_Uzor_36_68e57d6557.png'

navbar = dbc.Navbar(id='navbar', children=[
    dbc.Row([
        dbc.Col(html.Img(src=metro_logo, height='50px')),
        dbc.Col(
            dbc.NavbarBrand('ОБЩЕЕ ЧИСЛО НАРУШЕНИЙ РАБОТЫ ТРАМВАЕВ', style={'color': 'grey', 'fontSize': '25px', 'fontFamily': 'Arial'})
        )
    ], align='center'),
    dbc.Button(id='button', children='Загрузить xlsx файл', color='success')
])

card_component = [
    dbc.CardHeader('Card Header'),
    dbc.CardBody(
        [
            html.H5('Card Title', className='card-title'),
            html.P('This is some card content what we will be use.', className='card-body')
        ]
    )
]

# app.layout = html.Div(id='parent', children=[navbar])

app.layout = dbc.Container([
    dbc.Row([navbar]),
    dbc.Row([
        dbc.Col(dbc.Card(card_component, color='primary', inverse=True)),
        dbc.Col(dbc.Card(card_component, color='info', inverse=True)),
        dbc.Col(dbc.Card(card_component, color='secondary', outline=True))
    ])
    # dbc.Row([line_chart.line_graf(x=line_chart.number_of_crush, y=line_chart.month)])
], fluid=True)




if __name__ == '__main__':
    app.run_server(port=8056, debug=True)
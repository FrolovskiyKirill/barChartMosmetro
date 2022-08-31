import dash
from dash import dcc, Dash
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
mytext = dcc.Markdown(children="## ОБЩЕЕ ЧИСЛО НАРУШЕНИЙ РАБОТЫ ТРАМВАЕВ")

# Customize your own Layout
app.layout = dbc.Container([mytext])

# Run app
if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
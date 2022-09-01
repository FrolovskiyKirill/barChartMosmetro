import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import plotly.express as px
from plotly.graph_objs import Line
from plotly.graph_objs.scatter.marker import Line

external_stylesheets = ['styles/styles.css']

app = dash.Dash(external_stylesheets=external_stylesheets)

month = ['Январь<br>2021', 'Февраль<br>2021', 'Март<br>2021', 'Апрель<br>2021', 'Май<br>2021', 'Июнь<br>2021', 'Июль<br>2021', 'Август<br>2021', 'Сентябрь<br>2021', 'Октябрь<br>2021', 'Ноябрь<br>2021', 'Декабрь<br>2021']
number_of_crush = [217, 276, 335, 259, 268, 397, 327, 273, 201, 204, 179, 230]


def line_graf(x, y):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x, y=y,
                             mode="lines+markers+text",
                             name="Lines, Markers and Text",
                             text=number_of_crush,
                             marker_size=35,
                             marker_line_width=2,
                             marker_color='rgba(255, 182, 193, .9)',
                             textposition='middle center',
                             textfont=dict(
                                 family='arial',
                                 size=16,
                                 color='Black'
                             ),
                             line_shape='spline',
                             opacity=1)
                  )

    fig.add_annotation(x=10, y=0.1,
                        text="",
                        showarrow=False)

    fig.update_layout(title='ОБЩЕЕ ЧИСЛО НАРУШЕНИЙ РАБОТЫ ТРАМВАЕВ',
                      title_x=0.5,
                      xaxis_title='Период',
                      yaxis_visible=False,
                      yaxis_showticklabels=False
                      )

    fig.add_layout_image(
        dict(
            source="https://cis.mosmetro.ru/strapi/uploads/MM_Uzor_36_68e57d6557.png",
            xref="paper", yref="paper",
            x=0.95, y=1.2,
            sizex=0.2, sizey=0.2,
            xanchor="right", yanchor="bottom"
        )
    )

    # update layout properties
    fig.update_layout(
        autosize=True,
        height=500,
        width=1200,
        bargap=0.15,
        bargroupgap=0.1,
        barmode="stack",
        hovermode="x",
        margin=dict(r=20, l=20, b=75, t=125),
        title="ОБЩЕЕ ЧИСЛО НАРУШЕНИЙ РАБОТЫ ТРАМВАЕВ",
        title_font_size=30
    )

    fig.update_layout(template="plotly_white")

    return fig


app.layout = html.Div(children=[
    html.H1(id='H1',
            children='Hello Dash',
            style={'background-image': 'url(https://gorod-plus.tv/media/photos2/all/105977_875x438_q75.jpg)'}),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=line_graf(month, number_of_crush),
        style={'background-image': 'url(https://gorod-plus.tv/media/photos2/all/105977_875x438_q75.jpg)'}
    )
], style={'background-image': 'url(https://gorod-plus.tv/media/photos2/all/105977_875x438_q75.jpg)'}
)

if __name__ == '__main__':
    app.run_server(debug=True)

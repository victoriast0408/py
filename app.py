import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
import pandas as pd
import numpy as np

app=dash.Dash()
abcstat = pd.read_excel('abcjan2018bm.xlsx')
app.layout = html.Div([
    
    dcc.Graph(
        id ='scatter_chart',
        figure = {
            'data':[
                go.Bar(
                x = abcstat.Umsatzgruppe,
                y = abcstat.Betrag,
                )
            ],
            'layout': go.Layout(
                title = 'ABC Statistik',
                xaxis = {'title' : 'Umsatzgruppen'},
                yaxis = go.layout.YAxis(
                    tickmode = 'linear',
        tick0 = 0,
        dtick = 80
    ),
                height=500
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
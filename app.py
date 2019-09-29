import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import numpy as np

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#add excel file
abcstat = pd.read_excel('abcjan2018bm.xlsx')

# iloc 0:144 excludes the rest of the cells  and make the cell 145 the last one
trace1 = go.Bar(x=abcstat.bezeichnung.iloc[0:144], y=abcstat.betrag)
labels = abcstat.umsatzgruppe
values = abcstat.betrag



#app=dash.Dash()

# Boostrap CSS.
#external_css = ["https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
             #   "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css", ]

#for css in external_css:
   # app.css.append_css({"external_url": css})


app.layout = html.Div([
    
  
    html.Div(
        [
        #the first row
        dbc.Row(
        dbc.Col(html.Div("A single Column")),
        ),
            
        #the second row
        dbc.Row(
            [
        dbc.Col(html.Div("The first column")),
        dbc.Col(html.Div("The second column")),
        dbc.Col(html.Div("The third column")),
            ]
        ),
            
        #the third row
        dbc.Row(
        [
                dbc.Col(html.Div
             # the first histogram
             (dcc.Graph(
            id ='histogram1',
            figure = {
                'data':[
                    trace1
                ],
                'layout': go.Layout(
                   #title = 'ABC Statistics',
                   #xaxis = {'title' : 'Umsatzgruppen'},
                    yaxis = go.layout.YAxis(
                        tickmode = 'linear',
                        tick0 = 0,
                        dtick = 100
                    ),   
                )
            }
        ),   
               ), width=3
               ),
            dbc.Col(html.Div
             # the second histogram
             (dcc.Graph(
            id ='histogram2',
            figure = {
                'data':[
                    trace1
                ],
                'layout': go.Layout(
                   #title = 'ABC Statistics',
                   #xaxis = {'title' : 'Umsatzgruppen'},
                    yaxis = go.layout.YAxis(
                        tickmode = 'linear',
                        tick0 = 0,
                        dtick = 100,
                    ),   
                )
            }
        ),   
               )
               ),
            #dbc.Col(html.Div("One of the three column")),
        ]),
            # the fourth row
            dbc.Row(

                    dbc.Col(html.Div
                    # the third - chart
                        (dcc.Graph(
                        id='chart1',
                        # Use `hole` to create a donut-like pie chart
                        figure=go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
                            )
      ),
    ),
)





       

            
            
        ])
])
        
    
        
        
        
        
        


if __name__ == '__main__':
    app.run_server(debug=True)
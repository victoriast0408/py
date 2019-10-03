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
        #the first row: title, navigation, logo
        dbc.Row([
        dbc.Col(html.Div("Bakery Title")),
        dbc.Col(html.Div(
            dbc.Nav(
            [
               dbc.NavItem(dbc.NavLink("Active", active=True, href="http://google.com")),
               dbc.NavItem(dbc.NavLink("Another Link", href="#")),
               dbc.NavItem(dbc.NavLink("Other Link", href="#")),
               dbc.NavItem(dbc.NavLink("Disabled Link", disabled=True, href="#")),
            ], pills=True,)
        )),
        dbc.Col(html.Div("Logo"), width=2),
        ]),
            
        #the second row: data in numbers
        dbc.Row(
            [
        dbc.Col(html.Div(
            dbc.Card(
            dbc.CardBody(
            [
                html.H6("Monthly Income"),
                html.H4("CHF 34598.60"),
                dbc.CardLink("Link")
            ]
            )
        ))),
         dbc.Col(html.Div(
            dbc.Card(
            dbc.CardBody(
            [
                html.H6("Monthly Income"),
                html.H4("CHF 34598.60"),
                dbc.CardLink("Link")
            ]
            )
        ))),        
         dbc.Col(html.Div(
            dbc.Card(
            dbc.CardBody(
            [
                html.H6("Monthly Income"),
                html.H4("CHF 34598.60"),
                dbc.CardLink("Link")
            ]
            )
        ))),
         dbc.Col(html.Div(
            dbc.Card(
            dbc.CardBody(
            [
                html.H6("Monthly Income"),
                html.H4("CHF 34598.60"),
                dbc.CardLink("Link")
            ]
            ),
        ))),
         dbc.Col(html.Div(
            dbc.Card(
            dbc.CardBody(
            [
                html.H6("Monthly Income"),
                html.H4("CHF 34598.60"),
                dbc.CardLink("Link")
            ]
            )
        ))),
            ]
        ),
            
        #the third row: 2 graphs
        dbc.Row(
            [
       dbc.Col(html.Div
                       (dcc.Graph(
                       id='graph1',
                       ))
                       ),
      dbc.Col(html.Div
                       (dcc.Graph(
                       id='graph2',
                       ))
                       ),
            ]),
            
            
            # the fourth row: 2 graphs
            dbc.Row(
                [
                  dbc.Col(html.Div
                    # the second graph
                        (dcc.Graph(
                        id='graph3',
                        ))     
            ),
                dbc.Col(html.Div
                    # the second graph
                        (dcc.Graph(
                        id='graph4',
                        ))     
            ),
            ]),
            
            # the fifth row: 2 graphs
            dbc.Row(
            [
                dbc.Col(html.Div
                       (dcc.Graph(
                       id='graph5',
                       ))
                       ),
                dbc.Col(html.Div
                        (dcc.Graph(
                        id='graph6',
                        ))
                ),
                dbc.Col(html.Div
                        (dcc.Graph(
                        id='graph7',
                        ))
                )
                
            ]),

        
        
        
])
        
], className="container-fluid")
        
        
        
        
        


if __name__ == '__main__':
    app.run_server(debug=True)
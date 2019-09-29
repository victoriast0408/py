import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel('abcjan2018bm.xlsx')

labels = df.umsatzgruppe
values = df.betrag

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.show()



if __name__ == '__main__':
    app.run_server(debug=True)
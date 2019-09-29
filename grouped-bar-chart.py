import plotly.graph_objects as go
import pandas as pd

bills = pd.read_excel('billsjan2018.xlsx')

fig = go.Figure(data=[
    go.Bar(name='Paid cash', x=bills.date, y=bills.paid_cash),
    go.Bar(name='Paid card', x=bills.date, y=bills.paid_card),
    go.Bar(name='Paid customer card', x=bills.date, y=bills.paid_customer_card),
],

)
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()



if __name__ == '__main__':
    app.run_server(debug=True)
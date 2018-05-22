import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
#
# trace = go.Table(
#     header=dict(values=df.columns,
#                 fill = dict(color='#C2D4FF'),
#                 align = ['left'] * 5),
#     cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
#                fill = dict(color='#F5F8FF'),
#                align = ['left'] * 5))
#
# data = [trace]

# import plotly.plotly as py
# import plotly.graph_objs as go
#
# values = [[['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL<br>EXPENSES</b>']],
# [["Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
#   "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
#   "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
#   "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
#   "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad"]]]
#
#
# trace0 = go.Table(
#   type = 'table',
#   columnorder = [1,2],
#   columnwidth = [80,400],
#   header = dict(
#     values = [['<b>EXPENSES</b><br>as of July 2017'],
#                   ['<b>DESCRIPTION</b>']],
#     line = dict(color = '#506784'),
#     fill = dict(color = '#119DFF'),
#     align = ['left','center'],
#     font = dict(color = 'white', size = 12),
#     height = 40
#   ),
#   cells = dict(
#     values = values,
#     line = dict(color = '#506784'),
#     fill = dict(color = ['#25FEFD', 'white']),
#     align = ['left', 'center'],
#     font = dict(color = '#506784', size = 12),
#     height = 30
#     ))
#
# data = [trace0]


import plotly.plotly as py
import plotly.graph_objs as go

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

trace0 = go.Table(
    type='table',
    header=dict(
        values=[['<b>EXPENSES</b>'],
                ['<b>Q1</b>'],
                ['<b>Q2</b>'],
                ['<b>Q3</b>'],
                ['<b>Q4</b>']],
        line=dict(color='#506784'),
        fill=dict(color=headerColor),
        align=['left', 'center'],
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[
            ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
            [1200000, 20000, 80000, 2000, 12120000],
            [1300000, 20000, 70000, 2000, 130902000],
            [1300000, 20000, 120000, 2000, 131222000],
            [1400000, 20000, 90000, 2000, 14102000]],
        line=dict(color='#506784'),
        fill=dict(color=[[rowOddColor, rowEvenColor, rowOddColor,
                          rowEvenColor, rowOddColor]]),
        align=['left', 'center'],
        font=dict(color='#506784', size=11)
    ))

data = [trace0]

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import colorlover as cl

colors = cl.scales['5']['seq']['Blues']
data = {'Year' : [2010, 2011, 2012, 2013, 2014],
        'Color' : colors}
df = pd.DataFrame(data)


trace0 = go.Table(
  type = 'table',
  header = dict(
    values = ["Color", "<b>YEAR</b>"],
    line = dict(color = 'white'),
    fill = dict(color = 'white'),
    align = ['center'],
    font = dict(color = 'black', size = 12)
  ),
  cells = dict(
    values = [df.Color, df.Year],
    line = dict(color = [df.Color]),
    fill = dict(color = [df.Color]),
    align = 'center',
    font = dict(color = 'black', size = 11)
    ))

data1 = [trace0]


import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import colorlover as cl

colors = cl.scales['9']['seq']['Reds']
a = np.random.randint(low=0, high=9, size=10)
b = np.random.randint(low=0, high=9, size=10)
c = np.random.randint(low=0, high=9, size=10)


trace0 = go.Table(
  type = 'table',
  header = dict(
    values = ['<b>Column A</b>', '<b>Column B</b>', '<b>Column C</b>'],
    line = dict(color = 'white'),
    fill = dict(color = 'white'),
    align = 'center',
    font = dict(color = 'black', size = 12)
  ),
  cells = dict(
    values = [a,b,c],
    line = dict(color = [np.array(colors)[a],np.array(colors)[b],
                        np.array(colors)[c]]),
    fill = dict(color = [np.array(colors)[a],np.array(colors)[b],
                        np.array(colors)[c]]),
    align = 'center',
    font = dict(color = 'white', size = 11)
    ))

data2 = [trace0]


# py.iplot(data, filename = "alternating row colors")

fig = dict(data=data2, )

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div(
    children=dcc.Graph(
        figure=fig,
        style={'height': '100%', 'width': '100%'},
        id='my-graph'
    ),
)

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)

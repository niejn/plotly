layout=dict(width=650,
            height=400,
            autosize=False,
            annotations=[dict(font= dict(color='rgb(100,100,100)'),
                              showarrow=False,
                              text= 'sepal length: '+'{:.2f}'.format(df.loc[k, 'sepal length (cm)']),
                              x= df.loc[k, 'sepal length (cm)']-1,#here I subtracted 1 from the sepal length to avoid displaying
                                                                  #the text at the bar end
                              xref= 'x',
                              y= df.loc[k, 'target'],
                              yref= 'y') for k in range(len(df))]
       )

my_text=['(sepal length: '+'{:.2f}'.format(sl)+', sepal width:'+'{:.2f}'.format(sw)+')'+
  '<br>(petal length: '+'{:.2f}'.format(pl)+', petal width:'+'{:.2f}'.format(pw)+')'
  for sl, sw, pl, pw in zip(list(df['sepal length (cm)']), list(df['sepal width (cm)']),
                           list(df['petal length (cm)']), list(df['petal width (cm)'])) ]
text=my_text,
hoverinfo='text'

trace=dict(type='scatter',
              x=x, y=y,
              mode='markers',
              marker=dict(size=4, color='rgb(188, 20, 26)'),
              text=['aaaaaaaa', 'bbbbbbbbb'],
              hoverlabel=dict(bgcolor='rgba(188, 20, 26, 0.5)'),
              hoverinfo='text')

dcc.Graph(figure={
    'data': [{
        'x': ['2015-01-01', '2015-01-10 15:30:12', '2015-04-01'],
        'y': [2, 1, 5]
    }],
    'layout': {
        'xaxis': {
            'tickformat': '%y/%m'
        }
    }
})


import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
)

trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
)

data = [trace1, trace2]

layout = go.Layout(
    showlegend=False,
    annotations=[
        dict(
            x=2,
            y=5,
            xref='x',
            yref='y',
            text='max=5',
            showarrow=True,
            font=dict(
                family='Courier New, monospace',
                size=16,
                color='#ffffff'
            ),
            align='center',
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='#636363',
            ax=20,
            ay=-30,
            bordercolor='#c7c7c7',
            borderwidth=2,
            borderpad=4,
            bgcolor='#ff7f0e',
            opacity=0.8
        )
    ]
)

import plotly.plotly as py

trace = dict(
    x=[1, 2, 3,],
    y=[10, 30, 15],
    type='scatter',
    name='first trace',
    hoverinfo='none'
)

py.iplot([trace], filename='hoverinfo=none')

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='style-annotation')


import dash_core_components as dcc
import plotly.graph_objs as go

dcc.Graph(
    figure=go.Figure(
        data=[
            go.Bar(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker=go.Marker(
                    color='rgb(55, 83, 109)'
                )
            ),
            go.Bar(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker=go.Marker(
                    color='rgb(26, 118, 255)'
                )
            )
        ],
        layout=go.Layout(
            title='US Export of Plastic Scrap',
            showlegend=True,
            legend=go.Legend(
                x=0,
                y=1.0
            ),
            margin=go.Margin(l=40, r=0, t=40, b=30)
        )
    ),
    style={'height': 300},
    id='my-graph'
)
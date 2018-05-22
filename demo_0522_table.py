import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
trace = go.Table(
    header=dict(values=['A Scores', 'B Scores']),
    cells=dict(values=[[100, 90, 80, 90],
                       [95, 85, 75, 95]]))

data = [trace]
fig = dict(data=data,)

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_core_components as dcc
app = dash.Dash()
app.layout = html.Div([
    html.Div(
        className="row",
        children=[
            html.Div(
                className="six columns",
                children=[
                    html.Div(
                        children=dcc.Graph(
                            figure=fig,
                            style={'height': 1000},
                            id='my-graph'
                        )
                    )
                ]
            ),

        ]
    )
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
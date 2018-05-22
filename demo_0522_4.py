import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
app = dash.Dash()
# The Graph component shares the same syntax as the open-source plotly.py library. View the plotly.py docs to learn more.
x_list = [1, 2, 3]
y_list = [3, 1, 2]
my_text = ["x:{:.2f}".format(x) for x in x_list]
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)

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
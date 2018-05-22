import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # df.to_html()
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
    # return df.to_html()

app = dash.Dash()
temp = generate_table(df)
# app.layout = html.Div(children=[
#     html.H4(children=df.to_html()),
#     # generate_table(df)
#     # df.to_html()
# ])
data = [
            {'x': [0, 1, 2], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [0, 1, 2], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
        ]
months = ['2017-01-01', '2017-02-01', '2017-03-01']
app.layout = html.Div(children=[html.H1(children=''), html.Div(children='Discovered monthly'),
                                dcc.Graph(
                                    figure=go.Figure(
                                        data=data,
                                        layout=go.Layout(
                                            title='Streams', showlegend=True, barmode='stack',
                                            margin=go.Margin(l=200, r=0, t=40, b=20),
                                            xaxis=dict(tickvals=tickvals, ticktext=months,
                                                       title='months')
                                        )
                                    ),
                                    style={'height': 300},
                                    id='my-graph')
                                ])

if __name__ == '__main__':
    app.run_server(debug=True)
#
# class test(object):
#     def __init__(self):
#         self.months = ['2017-01-01', '2017-02-01', '2017-03-01']
#         self.data = [
#             {'x': [0, 1, 2], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#             {'x': [0, 1, 2], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#         ]
#
#         # X-Axis location for the ticks
#         self.tickvals = [0, 1, 2]
#
#     def plot_bar(self):
#         app.layout = html.Div(children=[html.H1(children=''), html.Div(children='Discovered monthly'),
#                                         dcc.Graph(
#                                             figure=go.Figure(
#                                                 data=self.data,
#                                                 layout=go.Layout(
#                                                     title='Streams', showlegend=True, barmode='stack',
#                                                     margin=go.Margin(l=200, r=0, t=40, b=20),
#                                                     xaxis=dict(tickvals=self.tickvals, ticktext=self.months,
#                                                                title='months')
#                                                 )
#                                             ),
#                                             style={'height': 300},
#                                             id='my-graph')
#                                         ])

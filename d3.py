import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

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
app.layout = html.Div(children=[
    html.H4(children=df.to_html()),
    # generate_table(df)
    # df.to_html()
])

if __name__ == '__main__':
    app.run_server(debug=True)
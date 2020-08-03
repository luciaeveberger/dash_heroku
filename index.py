import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layouts.layouts import layout1, layout2, layout3
from callbacks import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dash':
        return layout1
    elif pathname == '/model':
        return layout2
    elif pathname == '/admin':
        return layout3
    else:
        return layout1


if __name__ == '__main__':
    app.run_server(debug=True)
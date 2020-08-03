import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os

from app import app
from app import server
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
    server=app.server
    server.secret_key = os.environ.get('secret_key', 'secret_key')
    app.run_server(debug=True)
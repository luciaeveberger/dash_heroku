import dash_html_components as html
from dash_table import DataTable

twitter_feed = html.Div([
    html.Div(
        id="patient_volume_card",
        children=[
            html.Hr(),
            DataTable(
                id='table',
                data=[],
                sort_action='native',
                filter_action="native",
                style_table={'overflowY': 'scroll', },
                style_cell={'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                        "whiteSpace":"normal"}
            )
        ],
    ),

])
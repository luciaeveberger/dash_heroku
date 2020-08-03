from components.control_panel import generate_control_card,generate_historical_search, description_card
import dash_html_components as html
import dash_core_components as dcc
from components.twitter_feed import twitter_feed

world_map_tab = html.Div(
    id="app-container",
    children=[
        html.Div(
            id="right-column",
            className="three columns",
            children=[description_card(), generate_control_card()]
                     + [
                         html.Div(
                             ["initial child"], id="output-clientside", style={"display": "none"}
                         )
                     ],
        ),

        # Banner
        html.Div(
            id="right-column",
            className="nine columns",
            children=[
                html.H5("World Map"),
                dcc.Graph(id="map-graph"),
                dcc.Interval(
                id='interval-component',
                interval=40000,  # in milliseconds
                n_intervals=0),
                html.Hr(),
                html.Hr(),
                html.H5("Tweet Feed"),
                twitter_feed
                ]
        ),

    ],
)
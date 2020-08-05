from components.control_panel import generate_control_card,generate_historical_search, description_card
import dash_html_components as html
import dash_core_components as dcc
from components.twitter_feed import twitter_feed
from components.analysis_tab import analysis_tab


world_map_tab = html.Div(
    id="app-container",
    children=[
        # Banner
        html.Div(
            #className="right-column",
            children=[
                html.H5("World Map"),
                dcc.Graph(id="map-graph"),
                dcc.Interval(
                id='interval-component',
                interval=40000,  # in milliseconds
                n_intervals=0),
                html.Hr(),
                html.Hr(),
                ]
        ),

    ],
)
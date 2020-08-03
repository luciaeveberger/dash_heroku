from components.control_panel import generate_historical_search
import dash_html_components as html
import dash_core_components as dcc
from components.twitter_feed import twitter_feed

tweet_search_tab = html.Div(
    id="app-container",
    children=[
        # Banner
        html.Div(
            id="right-column",
            className="three columns",
            children=[generate_historical_search(),
                ]
        ),
        # Left column
        html.Div(
            id="left-column",
            className="nine columns",
            children=[html.Div(id='output_container')]
                     + [
                         html.Div(
                             ["initial child"], id="output-clientside", style={"display": "none"}
                         )
                     ],
        ),

    ],
)
import dash_html_components as html
from components.control_panel import generate_control_card,generate_historical_search, description_card
import dash_core_components as dcc
import numpy as np
import plotly.express as px


analysis_tab = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Graph(id="bar-chart", style={"width" : "100%"}),
                html.Hr(),
                html.Hr(),
                ]
        ),

    ],
)
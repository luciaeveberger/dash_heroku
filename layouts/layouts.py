import dash_core_components as dcc
import dash_html_components as html
from components.navigation import navigation
from components.tabs import tabs
from components.control_panel import description_card, generate_control_card

layout1 = html.Div(
    id="app-container",
    children=[
        # Banner
        navigation,
        html.Div(className="columns",
                 children=[tabs])

    ],
)

layout2 = html.Div(
    id="app-container", \
    children=[
        # Banner
        navigation,
        html.Div(
            id="right-column",
            className="eight columns",
            children=[
                html.H3("Model"),
            ]
        ),
        # Left column

    ],
)

layout3 = html.Div(
    id="app-container", \
    children=[
        # Banner
        navigation,
        html.Div(
            id="right-column",
            className="eight columns",
            children=[
                html.H3("ADMIN"),
            ]
        ),


    ],
)

import dash_html_components as html

analysis_tab = html.Div(
    id="app-container",
    children=[
        # Banner
        html.Div(
            id="right-column",
            className="nine columns",
        ),
        html.Div(
            id="left-column",
            className="three columns",)
        ]
)

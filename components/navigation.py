import dash_html_components as html
import dash_bootstrap_components as dbc

button_group = dbc.ButtonGroup(
    [dbc.Button("DASH", href='/dash', active=True), dbc.Button("MODEL", href='/model'), dbc.Button("ADMIN", href='/admin')],
    size="lg",
)

navigation = html.Div(
    id="banner",
    className="banner",
    children=[
        html.Div(children=[button_group],
                 id="button_move")]
)
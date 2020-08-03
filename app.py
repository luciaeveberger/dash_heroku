import dash
import json
import dash_bootstrap_components as dbc
import dash_auth


with open('_dashboard_login.json') as dashboard_login:
    data = json.load(dashboard_login)
    VALID_USERNAME_PASSWORD_PAIRS = data['VALID_USERNAME_PASSWORD_PAIRS']


app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

server = app.server
app.config.suppress_callback_exceptions = True
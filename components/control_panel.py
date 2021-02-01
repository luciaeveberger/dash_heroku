import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from datetime import datetime as dt

type_of_models = ['SUPERVISED', 'UNSUPERVISED']
filter_streams = ['covid', 'trump', 'other']
languages = ['en', 'fr', 'de']
today = dt.today()

switches = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Historical Search"},
            ],
            switch=True,
            id='toggle',
            value='0',
        ),
    ]
)


def description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Live Stream Filters"),
        ],
    )


def generate_control_card():
    """

    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
            html.P("Filters will be applied to your dashboard",
                   id='intro'),
            html.P("Model Type"),
            dcc.Dropdown(
                id="model type",
                options=[{"label": i, "value": i} for i in type_of_models],
                value=type_of_models[0],
            ),
            html.P("Filter stream"),
            dcc.Input(id='filter_terms', type='text', placeholder='Search Words'),
            html.Br(),
            html.Br(),
            html.Button(id='submit-button', n_clicks=0, children='Submit'),
            html.A(html.Button(id="reset-btn", children="Reset", n_clicks=0),
                   href='/'),

            html.Br(),
            html.Br(),
            html.Div(id="output-state"),
            html.Div(id="reset-state"),

        ],
    )


def generate_historical_search():
    return html.Div(id="control-card",
        children=[
        html.H5("Historical Search"),
        html.P("Search historical feeds",
                   id='intro'),
        html.Div(className='', children=[
            dcc.Input(id='search_words', type='text', placeholder='Search Words', value='covid, trump'),
            html.Br(),
            html.Br(),
            dcc.DatePickerRange(
                id="date-picker-select",
                start_date=dt(today.year, today.month, today.day),
                end_date=dt(today.year, today.month, today.day),
                min_date_allowed=dt(2014, 1, 1),
                max_date_allowed=dt(today.year, today.month, today.day),
                initial_visible_month=dt(today.year, today.month, 1),
            ),
            html.Br(),
            html.Br(),
            dcc.Dropdown(
                id="language_select",
                options=[{"label": i, "value": i} for i in languages],
                multi=False,
                value=languages[0],
            ),
            html.Br(),
            html.Br(),
            dcc.Input(id='geo_code', type='text', placeholder='Geocode', value=''),

        ]),
        dcc.Slider(
            id='max_tweets',
            min=0,
            max=100,
            step=0.5,
            value=10,
            marks={
                0: '0 Tweets',
                50: '50 Tweets',
                100: '100 Tweets'
            },
        ),
        html.Br(),
        html.Button(id='submit_search', n_clicks=0, children='Submit Search'),


    ])

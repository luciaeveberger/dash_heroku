import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from components.control_panel import generate_control_card,generate_historical_search, description_card
#generate_historical_search,\
    #generate_control_card, description_card

tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="World Map", tab_id="tab-1"),
                dbc.Tab(label="Other Analysis", tab_id="tab-2"),
                dbc.Tab(label="Historical Search", tab_id="tab-3"),
            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div(id="content"),
    ]
)

world_map_tab = html.Div(
    id="app-container",
    children=[
        # Banner
        html.Div(
            id="right-column",
            className="nine columns",
            children=[
                ]
        ),
        # Left column
        html.Div(
            id="left-column",
            className="three columns",
            children=[description_card(), generate_control_card()]
                     + [
                         html.Div(
                             ["initial child"], id="output-clientside", style={"display": "none"}
                         )
                     ],
        ),

    ],
)


#
# html.Div([
#     html.Div(
#         children=[  html.Div(
#
#         id="left-column",
#         className="three columns",
#         children=[generate_control_card()])])

# world_map_tab = html.Div([
#     html.Div(children=[id="left-column", className="three columns"])])
            # id="right-column",
            #  className="nine columns",
            #  children=[dcc.Graph(id="map-graph"),
            #            dcc.Interval(
            #     id='interval-component',
            #     interval=40000,  # in milliseconds
            #     n_intervals=0),
            # html.Hr(),
            # html.B("Tweet Feed"),
            # html.Hr()]




# html.Div(children=[id="right-column", className="nine columns"])
            # children=[
            # dcc.Graph(id="map-graph"),
            # dcc.Interval(
            #     id='interval-component',
            #     interval=40000,  # in milliseconds
            #     n_intervals=0,
            # ),
            # html.Hr(),
            # html.B("Tweet Feed"),
            # html.Hr()]]
        #)])
        # # Left column
        # html.Div(
        #     id="left-column",
        #     className="three columns",
        #     children=[]#description_card(), generate_control_card() ]
        #              + [
        #                  html.Div(
        #                      ["initial child"], id="output-clientside", style={"display": "none"}
        #                  )
        #              ],
        # ),






#
# tabs_3_content = html.Div(
#     children=[
#         html.H3("Search Historically"
#                 ),
#         generate_historical_search()
#     ])

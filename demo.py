# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
#from components.control_panel import control_panel
from components.control_panel import generate_control_card,generate_historical_search, description_card
from components.world_map_tab import world_map_tab
from callbacks.callbacks import callbacks


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout =  html.Div(
    id="patient_volume_card",
    children=[generate_control_card(),
        html.Div(
            children=[
             dcc.Tabs([
        dcc.Tab(label='Tab one', children=[
                world_map_tab
            # dcc.Graph(
            #     figure={
            #         'data': [
            #             {'x': [1, 2, 3], 'y': [4, 1, 2],
            #                 'type': 'bar', 'name': 'SF'},
            #             {'x': [1, 2, 3], 'y': [2, 4, 5],
            #              'type': 'bar', 'name': u'Montréal'},
            #         ]
            #     }
            # )
        ]),
        dcc.Tab(label='Tab two', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [1, 4, 1],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [1, 2, 3],
                         'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )
        ]),
        dcc.Tab(label='Tab three', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [2, 4, 3],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [5, 4, 3],
                         'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )
        ]),
    ])
                
                ]
        ),

    ],
)




# html.Div(
#     children[generate_control_card()

#     ]


#     [
   
# ])
app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=True)
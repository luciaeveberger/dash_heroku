import requests
import os
import json
from settings import API_HOSTNAME
import dash_html_components as html

from app import app
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_table


@app.callback(Output('output_container', 'children'),
              [Input('submit_search', 'n_clicks')],
              [State('search_words', 'value'),
               State('language_select', 'value'),
               State('max_tweets', 'value')
               ]
              )
def search_historically(n_clicks, search_words, language_select, max_tweets):
    if n_clicks > 0:
        dict_json = {
            "count": "",
            "date_since": "",
            "geocode": "",
            "included_entities": "",
            "lang": language_select,
            "max_items": max_tweets,
            "results_type": "",
            "search_words": search_words,
            "since_id": ""
        }
        response = requests.post(os.path.join(API_HOSTNAME, 'get_tweets/search_tweets'),
                                 json=dict_json)
        output = json.loads(response.text)
        d = []
        for p in output:
            d.append(
                {
                    'Text': p['text'],
                    'User': p['user']['name'],
                    'Created At': p['created_at']

                }
            )
        data_frame = pd.DataFrame(d)
        return html.Div(id='search-details',
                        children=[html.Button('save search'),
                                  dash_table.DataTable(
                                      id='historical_table',
                                      columns=[{"name": i, "id": i} for i in data_frame.columns],
                                      data=data_frame.to_dict('records'),
                                      filter_action="native",
                                      sort_action='native',
                                      style_cell={

                                          'minWidth': '300px', 'width': '300px', 'maxWidth': '300px',
                                          'whiteSpace': 'normal'
                                      }
                                  )]
                        )

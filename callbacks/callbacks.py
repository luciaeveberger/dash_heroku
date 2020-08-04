import requests
import os
import time

from settings import API_HOSTNAME

from app import app
from dash.dependencies import Input, Output, State
from components.world_map_tab import world_map_tab
from components.analysis_tab import analysis_tab
from components.tweet_search_tab import tweet_search_tab
import callbacks.twitter_feed_callback
import callbacks.twitter_search_callbacks
from callbacks.twitter_feed_callback import clear_data

@app.callback(Output('controls-container', 'style'),
              [Input('toggle', 'value')])
def toggle_container(toggle_value):
    if len(toggle_value) > 1:
        return {'display': 'block'}
    else:
        return {'display': 'none'}


# tabs
@app.callback(Output("content", "children"),
              [Input("tabs", "active_tab")])
def switch_tab(at):
    #@todo: figure out if necessary
    if at == "tab-1":
        return world_map_tab
    elif at == "tab-2":
        return analysis_tab
    elif at == "tab-3":
        return tweet_search_tab


@app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('filter_terms', 'value')])
def update_output(n_clicks, input1):
    if n_clicks > 0:
        dict_json = {"stream_name": input1}
        # start_stream = requests.post(os.path.join(API_HOSTNAME, 'get_tweets/'),
        #                              json=dict_json)

        clear_data()
        time.sleep(1)

        # if start_stream.status_code == 200:
        return 'streaming on {}'.format(input1)
        # else:
        #     return 'failed to connect to twitter stream'

@app.callback(Output('reset-state', 'children'),
              [Input('reset-btn', 'n_clicks')],
              [State('filter_terms', 'value')])
def reset_output(n_clicks, input1):
    if n_clicks > 0:
        input1 = ""
        clear_data()
        time.sleep(1)
        return "reset data"

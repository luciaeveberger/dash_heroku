from app import app
from dash.dependencies import Input, Output, State
import pandas as pd
import requests
import os
import json
from settings import API_HOSTNAME
from plotly import graph_objs as go
from settings import MAPBOX_ACCESS_TOKEN


import plotly.express as px

HEATWAVE_DATA = "DUMMY_DATA/heatwave.json"
ARCTIC_DATA = "DUMMY_DATA/arctic.json"

colours = px.colors.sequential.Plasma
tweet_feed = pd.DataFrame(columns=['id_str', 'received_at', 'user', 'text', 'label', 'user_city'])

LABELS = {
    "affected_people": "#F4EC15",
    "other_useful_information": "#1f77b4",
    "disease_transmission": "#BBEC19",
    "disease_signs_or_symptoms":"#9DE81B",
    "prevention":"#80E41D",
    "treatment":"#66E01F",
    "not_related_or_irrelevant": "#4CDC20",
    "deaths_reports":"#34D822",
}


def clear_data():
    """
    clears the dataframe data
    """
    global tweet_feed
    tweet_feed = tweet_feed.iloc[0:0]


def get_streaming_data(prev_filter_term, curr_filter_term):
    dict_json = {"stream_name": curr_filter_term}
    cwd = os.getcwd()
    DATA = HEATWAVE_DATA
    
    if curr_filter_term == 'heatwave':
        DATA = HEATWAVE_DATA

    if curr_filter_term == 'arctic':
        DATA = ARCTIC_DATA

    parsed_data = []
    with open(os.path.join(cwd, DATA)) as f:

        get_information_from_stream = json.load(f)
        stream = get_information_from_stream

        for i in range(0, len(stream)):

            coordinates = []
            if stream[i]['tweet']['geolocation']['user_cities']:
                coordinates.append([stream[i]['tweet']['geolocation']['user_cities'][0]])
                coordinates.append([stream[i]['tweet']['geolocation']['user_cities'][1]])
                if stream[i]['tweet']['id_str'] not in tweet_feed.id_str.values:
                    tweet_feed.loc[len(tweet_feed) + i] = [stream[i]['tweet']['id_str'],
                                                           stream[i]['tweet']['created_at'],
                                                           stream[i]['tweet']['user']['name'],
                                                           stream[i]['tweet']['text'],
                                                           stream[i]['label'],
                                                           coordinates]
                                            


    series_histogram = tweet_feed['label'].value_counts()

    return tweet_feed.to_dict('records'), series_histogram


@app.callback(
    [Output("map-graph", "figure"),
     Output("table", "data"),
     Output('table', 'columns'),
     Output("bar-chart", "figure")
     ],
    [
        Input("interval-component", "n_intervals"),
        Input("filter_terms", "value"),
        Input('submit-button', 'n_clicks'),
    ],
    [State("map-graph", "relayoutData"),
     State('filter_terms', 'value')],
)
def update_graph(n_intervals, current_filter_term, nclicks, relayoutData, previous_filter_term):
    parsed_data = []
    if nclicks > 0:
        data, series_histogram = get_streaming_data(current_filter_term, previous_filter_term)
        series_histogram = series_histogram.to_frame()
        series_histogram['count'] = series_histogram.index

        colors = [] 
        for key in LABELS.keys():
            parsed_data.append(go.Scatter(x=[None], y=[None], mode='markers',
                           marker=dict(size=5, color=LABELS[key]),
                           legendgroup=key, showlegend=True, name=key))

            if key not in series_histogram['label']:
                series_histogram.loc[len(series_histogram)+1] = [0, key]

        series_histogram['colors'] = series_histogram['count'].map(LABELS)
        fig = go.Figure([go.Bar(x=series_histogram['count'], 
            y=series_histogram['label'], 
            marker={'color': series_histogram['colors']})])
        
    else:
        data = []
        series_histogram = []
        fig = px.bar()
    try:
        lat_initial = (relayoutData['mapbox.center']['lat'])
        lonInitial = (relayoutData['mapbox.center']['lon'])
        zoom = (relayoutData['mapbox.zoom'])
    except:
        lat_initial = 40.7272
        lonInitial = -73.991251
        zoom = 0

    bearing = 0
    
    for value in data:
        parsed_data += [
            go.Scattermapbox(
                lat=value['user_city'][0],
                lon=value['user_city'][1],
                mode="markers",
                hoverinfo="text",
                text=value['text'],
                showlegend=False,
                name=value['label'],
                legendgroup=value['label'],
                marker=dict(
                    showscale=False,
                    size=5,
                    color=LABELS.get(value['label']),
                ),

            )
        ]


    figure = go.Figure(
        data=parsed_data,
        layout=go.Layout(
            autosize=True,
            margin=go.layout.Margin(l=0, r=0, t=0, b=0),
            showlegend=True,
            mapbox=dict(
                accesstoken=MAPBOX_ACCESS_TOKEN,
                center=dict(lat=lat_initial, lon=lonInitial),  # 40.7272  # -73.991251
                style="dark",
                bearing=bearing,
                zoom=1,
            ),
            updatemenus=[
                dict(
                    buttons=(
                        [
                            dict(
                                args=[
                                    {
                                        "mapbox.zoom": 12,
                                        "mapbox.center.lon": "-73.991251",
                                        "mapbox.center.lat": "40.7272",
                                        "mapbox.bearing": 0,
                                        "mapbox.style": "dark",
                                    }
                                ],
                                label="Reset Zoom",
                                method="relayout",
                            )
                        ]
                    ),
                    direction="left",
                    pad={"r": 0, "t": 0, "b": 0, "l": 0},
                    showactive=False,
                    type="buttons",
                    x=0.45,
                    y=0.02,
                    xanchor="left",
                    yanchor="bottom",
                    bgcolor="#323130",
                    borderwidth=1,
                    bordercolor="#6d6d6d",
                    font=dict(color="#FFFFFF"),
                )
            ],
        ),
    )
    figure.update_layout(legend=dict(bordercolor='rgb(100,100,100)', 
                                  borderwidth=1,
                                  itemclick='toggleothers',
                                  x=0.78,
                                  y=0))

    tblcols = [{'name': 'id_str', 'id': 'id_str'},
               {'name': 'received at', 'id': 'received_at'},
               {'name': 'user', 'id': 'user'},
               {'name': 'text', 'id': 'text'},
               {'name': 'label', 'id': 'label'},
               {'name': 'city', 'id': 'city'},
               ]


    return figure, data, tblcols, fig

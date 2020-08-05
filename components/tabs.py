import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from components.control_panel import generate_control_card,generate_historical_search, description_card
from components.world_map_tab import world_map_tab
from components.twitter_feed import twitter_feed
from components.analysis_tab import analysis_tab
from components.control_panel import generate_historical_search

tabs_styles = {
    'height': '20px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}


tabs =  html.Div(
    id="app-container",
    children=[
        html.Div(
            id='control_panel',
            className="three columns right-column",
            children=[html.Div(id='generic_call_back', children=[description_card(), 
                      generate_control_card()]), 
                    html.Div(id='historical_search', style={"display": "none"}, children=[
                      generate_historical_search()], 
                      ), 
        
        ]),
        # Banner
        html.Div(id="tabs",
            className="nine columns right-column",
            children=[
             dcc.Tabs([
            dcc.Tab(label='World map', style=tab_style, selected_style=tab_selected_style, 
             children=[
                world_map_tab
        ]),
        dcc.Tab(label='Tweet Feed',  style=tab_style, selected_style=tab_selected_style, children=[
            twitter_feed
        ]),
        dcc.Tab(label='Classification', style=tab_style, selected_style=tab_selected_style, children=[
            analysis_tab
           
        ]),
        dcc.Tab(label='Historical',  value='switch_controls', style=tab_style, selected_style=tab_selected_style, children=[
        ]),
    ])
                
                ]
        ),

    ],
)




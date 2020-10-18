import dash
import dash_bootstrap_components as dbc
import dash_auth

#'https://codepen.io/chriddyp/pen/bWLwgP.css', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css', 'https://codepen.io/chriddyp/pen/brPBPO.css'
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']
appDash = dash.Dash(__name__, external_stylesheets=external_stylesheets)
appDash.config.suppress_callback_exceptions = True
appDash.title = 'Datos Globales'
server = appDash.server

import flask
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from layouts import login_form, layout_bbva_pantalla1, layout_simuladores, layout_ahorro, layout_choque, layout_consejo, layout_tips, layout_segmentacion
import callbacks
import os
#from app import appDash


#The page content
appDash.layout = html.Div([
	dcc.Store(id='local', storage_type='local'),
	dcc.Location(id='url', refresh=False),
	html.Div(id='page-content'),

])
#res = flask.make_response()
#res.set_cookie("name", value="I am cookie")

# Update the index
@appDash.callback(Output('page-content', 'children'),
			  [Input('url', 'pathname')])
def display_page(pathname):
	
	

	if pathname == '/login':
		return login_form
	if pathname == '/hackathon':
		return layout_bbva_pantalla1
	if pathname == '/simuladores':
		return layout_simuladores
	if pathname == '/ahorro':
		return layout_ahorro
	if pathname == '/choque':
		return layout_choque
	if pathname == '/consejo':
		return layout_tips  
	if pathname == '/segmentacion':
		return layout_segmentacion
	
	else:	
		return html.H1('404', style = {'textAlign': 'center', 'fontSize': '40'})
			



# ------------------------------------------------------------------------------
if __name__ == '__main__':
	appDash.run_server(debug = True, port = 8887)


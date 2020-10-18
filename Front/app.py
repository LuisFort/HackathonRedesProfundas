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
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from layouts import login_form, layout_bbva_pantalla1, layout_simuladores, layout_ahorro, layout_choque, layout_consejo, layout_tips
import callbacks
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
	
	else:	
		return html.H1('404', style = {'textAlign': 'center', 'fontSize': '40'})
			



@appDash.callback(
	[Output(component_id='output_container', component_property='children'),
	 Output(component_id='grafica1', component_property='figure'),],

	[Input(component_id='edad_inicial', component_property='value'),
	 Input(component_id='edad_final', component_property='value'),
	 Input(component_id='ahorro_mensual', component_property='value'),
	 Input(component_id='meta', component_property='value'),
	],

	
)
def update_graph(edad, retiro_edad_meta, ahorro_mes, dinero_meta):
  print(edad, retiro_edad_meta)
  ahorro_obj = round(dinero_meta/((retiro_edad_meta - edad)*12),2)
  print(ahorro_obj)
  if (ahorro_mes + ahorro_mes*.5) > (ahorro_obj - ahorro_obj*0.3):
    fig = go.Figure(go.Indicator(
        mode = "number+gauge+delta", value = ahorro_mes,
        domain = {'x': [0.1, 1], 'y': [0, 1]},
        title = {'text' :"<b>Ahorro</b>"},
        delta = {'reference': ahorro_obj},
        gauge = {
            'shape': "bullet",
            'bar': {'color': "black"},
            'axis': {'range': [None, ahorro_mes + ahorro_mes*.5]},
            'threshold': {
                'line': {'color': "blue", 'width': 5},
                'thickness': 1,
                'value': ahorro_obj},
            'steps': [
                {'range': [0, ahorro_obj - ahorro_obj*0.3], 'color': "red"},
                {'range': [ahorro_obj - ahorro_obj*0.3, ahorro_obj], 'color': "yellow"},
                {'range': [ahorro_obj, ahorro_mes + ahorro_mes*.5], 'color': "green"}]}))
    fig.update_layout(height = 400)
    explicacion = """La barra negra indica que tan cerca estás de lograr tu meta, si llega al rojo quiere decir que 
    estás lejos de tu meta. Si llega al naranja quiere decir que estás cerca. Y si llega a verde quiere decir que tu meta la cumplirás.
    En la derecha encontrarás un undicador de la cantidad que te faltaría o te sobraría de tu ahorro mensual para lograr tu meta"""
    return explicacion, fig
    
  elif ahorro_mes < (ahorro_obj - ahorro_obj*0.3):
      fig = go.Figure(go.Indicator(
        mode = "number+gauge+delta", value = ahorro_mes,
        domain = {'x': [0.1, 1], 'y': [0, 1]},
        title = {'text' :"<b>Ahorro</b>"},
        delta = {'reference': ahorro_obj},
        gauge = {
            'shape': "bullet",
            'bar': {'color': "black"},
            'axis': {'range': [None, ahorro_mes + ahorro_mes*.5]},
            'threshold': {
                'line': {'color': "blue", 'width': 5},
                'thickness': 1,
                'value': ahorro_obj},
            'steps': [
                {'range': [0, ahorro_mes + ahorro_mes*.5], 'color': "red"},
                {'range': [ahorro_obj - ahorro_obj*0.3, ahorro_obj], 'color': "yellow"},
                {'range': [ahorro_obj, ahorro_mes + ahorro_mes*.5], 'color': "green"}]}))
      fig.update_layout(height = 400)

      explicacion = """La barra negra indica que tan cerca estás de lograr tu meta, si llega al rojo quiere decir que 
	    estás lejos de tu meta. Si llega al naranja quiere decir que estás cerca. Y si llega a verde quiere decir que tu meta la cumplirás.
	    En la derecha encontrarás un undicador de la cantidad que te faltaría o te sobraría de tu ahorro mensual para lograr tu meta"""
      return explicacion, fig
    


# ------------------------------------------------------------------------------
if __name__ == '__main__':
	appDash.run_server(debug = True, port = 8887)


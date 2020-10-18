import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
from app import appDash
import json
import time
import requestBack as rb
import plotly.graph_objects as go



@appDash.callback(
    [ Output('redirect', 'children'),
      Output(component_id='hidden_div_for_updateST_callback_login', component_property='children'),
      Output("alert-auto", "is_open"),
      Output("alert-auto2", "is_open"),
      Output("alert-auto3", "is_open")
      ],
    [Input('submit-val', 'n_clicks'),
     Input('local', 'data')],

    [State('mail', 'value'),
     State('pass', 'value'),
     State("alert-auto", "is_open"),
     State("alert-auto2", "is_open"),
     State("alert-auto3", "is_open")])
def update_output(n_clicks, storage, value, value2, is_open, is_open2, is_open3):
    print(storage)
    print(value, value2)
    
    if not storage :

        if value and value2 :
            tokens = rb.rLogin(value, value2)
            if tokens:
                return  dcc.Location(pathname="/dashboard", id = 'redirecting'), dcc.Store(id = 'local', storage_type = 'local', data = tokens), is_open, is_open2, is_open3

            return None, None, not is_open, is_open2, is_open3

        elif value and not value2 :
            return None, None, is_open, not is_open2, is_open3

        elif not value and value2 :
            return None, None, is_open, is_open2, not is_open3

        return None, None, is_open, is_open2, is_open3

    return  dcc.Location(pathname="/dashboard", id = 'redirecting'), None, is_open, is_open2, is_open3


@appDash.callback(
	[Output(component_id='output_container', component_property='children'),
	 Output(component_id='grafica1', component_property='figure'),],

	[Input(component_id='edad_ini', component_property='value'),
	 Input(component_id='edad_final', component_property='value'),
	 Input(component_id='ahorro_mensual', component_property='value'),
	 Input(component_id='meta', component_property='value'),
	],

	
)
def update_graph(edad, edad_retiro_meta, ahorro_mes, dinero_meta):
  print(edad, edad_retiro_meta)
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
    fig.update_layout(height = 250)
    return fig
    
  elif ahorro_mes < (ahorro_obj - ahorro_obj*0.3):
      fig = go.Indicator(
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
                  {'range': [ahorro_obj, ahorro_mes + ahorro_mes*.5], 'color': "green"}]})
      fig.update_layout(height = 250)
      return fig
    



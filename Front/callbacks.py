import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
from app import appDash
import json
import time
import requestBack as rb
import plotly.graph_objects as go


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
      En la derecha encontrarás un indicador de la cantidad que te faltaría o te sobraría de tu ahorro mensual para lograr tu meta"""
      return explicacion, fig
    

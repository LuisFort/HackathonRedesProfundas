import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
from app import appDash
import json
import time
import requestBack as rb
import plotly.graph_objects as go
import boto3
import json


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
    En la derecha encontrarás un indicador de la cantidad que te faltaría o te sobraría de tu ahorro mensual para lograr tu meta"""
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


@appDash.callback(
  Output(component_id='output_container2', component_property='children'),
  [Input('submit-val', 'n_clicks')],
  
  )
def update_output(n_clicks):

  
  changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
  if 'submit-val' in changed_id:
    


    photo='prueba1.jpg'
    bucket='aws-deepracer-50376646-a8ec-4ddd-b4ec-370529022492'
    client=boto3.client('rekognition',region_name='us-east-1')

    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])

    print('Detected faces for ' + photo) 
    faces = []   
    for faceDetail in response['FaceDetails']:
        
        faces.append(json.dumps(faceDetail, indent=4, sort_keys=True))
    if len(faces) > 0 :
      return  str(faces[0]['AgeRange']['High']) + str(faces[0]['Gender']['Value'])
    return "Información no obtenida"
    

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

login_form = html.Div([
    dcc.Store(id='local', storage_type='local'),

    html.Div(id = 'bg'),

    html.Div(
      children = [
        html.Div(className = 'div-form', children = [

            html.H1("Inicia Sesión", style={ 'textAlign': 'left', 'marginBottom': '30px', 'marginTop': '50%', 'marginRight': '80px'}),
            html.Label("Correo electrónico", style={ 'textAlign': 'left', 'fontSize': '130%', 'marginBottom': '5px', 'marginRight': '40%'}),
            dcc.Input(id = 'mail', placeholder='Correo electrónico', name='username', type='text', style = {'width': '75%', 'paddingLeft': '20px', 'marginBottom': '15px'}),
            html.Label("Contraseña", style={ 'textAlign': 'left', 'fontSize': '130%', 'marginBottom': '5px', 'marginRight': '53%'}),
            dcc.Input(id = 'pass', placeholder='Contraseña', name='password', type='password', style = {'width': '75%', 'paddingLeft': '20px', 'marginBottom': '15px',}),
            #html.Button('Iniciar sesión', type='Submit', id = 'submit-val', n_clicks=0),
            dbc.Button("Iniciar sesión", id="submit-val", outline=True, color="secondary", className = 'newButton'),
            
            dbc.Toast(
              "Usuario o contraseña incorrectos",
              id = "alert-auto",
              className = 'alertMP',
              is_open = False,
              duration = 1500,
              style = {"position": "fixed", "top": 66, "right": 1, "width": 320, 'backgroundColor': 'red', 'fontSize': '145%', 'textAlign': 'center', 'padding': '30px 30px', 'borderRadius': '10px'},
            ),
            dbc.Toast(
              "Ingresa una contraseña válida",
              id = "alert-auto2",
              className = 'alertMP',
              is_open = False,
              duration = 1500,
              style = {"position": "fixed", "top": 66, "right": 1, "width": 320, 'backgroundColor': 'red', 'fontSize': '145%', 'textAlign': 'center', 'padding': '30px 30px', 'borderRadius': '10px'},
            ),
            dbc.Toast(
              "Ingresa un correo válido",
              id = "alert-auto3",
              className = 'alertMP',
              is_open = False,
              duration = 1500,
              style = {"position": "fixed", "top": 66, "right": 1, "width": 320, 'backgroundColor': 'red', 'fontSize': '145%', 'textAlign': 'center', 'padding': '30px 30px', 'borderRadius': '10px'},
            ),
            html.Div(id='redirect'),
            html.Div(id="hidden_div_for_updateST_callback_login")
        ]),
      ],
      style = {'width': '30%', 'paddingLeft': '20px'}
    ),
    

])



layout_bbva_pantalla1 = html.Div([
      
        html.Img(src = 'assets/header1.png', style = {'width': '100%', 'height': 80, 'marginBottom': 15}),

        html.Div( className='row',  # Define the row element
          children=[
            html.Div(id = 'controls',className='six columns', style = {'backgroundColor': '#C7E7F5', 'marginLeft': 20, 'height': 650, 'borderRadius': '10px'},
              children = [
                html.Iframe(src = "https://creator.us.uneeq.io/try/d64f1e78-0122-4473-83f1-cf0c102eaa1f", style = {"width": '100%', "height": "100%", 'borderRadius': '10px'} )
              ]
            ),
            html.Div(id = 'controls',className='six columns div-elementos-centro', style = {'backgroundColor': '#C7E7F5', 'marginLeft': 20, 'height': 650, 'borderRadius': '10px'},
              children = [
                html.H1('aqui va todo esto'),
                html.A(dbc.Button("Continuar", id="submit-val", outline=True, color="secondary", className = 'newButton'),  href = '/simuladores')
                #html.Button("Continuar", id="submit-val",  className = 'newButton', href = '/simuladores')
              ]
            )
          ]
        )       
    
  ])

#'diplay': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'flexDirection': 'column'

layout_simuladores=html.Div([
      
        html.Img(src = 'assets/header1.png', style = {'width': '100%', 'height': 80, 'marginBottom': 15}),
        html.H1("Tipos de Simuladores", style = {'textAlign': 'center', 'fontSize': '30','marginBottom': '5px', 'marginTop': '2%','color':'blue'}),
        html.Div( className='row',  # Define the row element
          children=[
            html.Div(id = 'controls',className='four columns', style = {'backgroundColor': '#C7E7F5', 'marginLeft': 30, 'height': 550, 'borderRadius': '10px'},
              children = [
                    html.H2('Simulador de Ahorro',style = {'textAlign': 'center', 'fontSize': '30','marginBottom': '5px', 'marginTop': '5%','color':'blue'}),
                  #  html.Img(src = 'assets/puerco.png', style = {'width': '95%', 'height':'70%','text-Align': 'center'}),
                    html.A( html.Img(src = 'assets/puerco.png', style = {'width': '95%', 'height':'70%','text-Align': 'center'}),href='http://127.0.0.1:8887/ahorro'),
                    html.H6('Conoce tus finanzas y prepara un mejor futuro, aprende a ahorrar y gastar.',style = { 'margin': 10, 'color': 'black'})
              ]
            ),
            html.Div(id = 'controls',className='four columns', style = {'backgroundColor': '#C7E7F5', 'marginLeft': 30, 'height': 550, 'borderRadius': '10px'},
              children = [
                html.H2('Simulador de Choque',style = {'textAlign': 'center', 'fontSize': '30','marginBottom': '5px', 'marginTop': '5%','color':'blue'}),
               #  html.Img(src = 'assets/alerta.png', style = {'width': '95%', 'height':'70%','text-Align': 'center'}),
                 html.A( html.Img(src = 'assets/alerta.png', style = {'width': '95%', 'height':'70%','text-Align': 'center'}),href='http://127.0.0.1:8887/choque'),
                 html.H6('No dejes que los imprevistos te hagan sentir mal dejandote en una situacion complicada.',style = { 'margin': 10, 'color': 'black'})
              ]
            ),
            html.Div(id = 'controls',className='four columns', style = {'backgroundColor': '#C7E7F5', 'marginLeft': 30, 'height': 550, 'borderRadius': '10px'},
              children = [
                html.H2('Consejos',style = {'textAlign': 'center', 'fontSize': '30','marginBottom': '5px', 'marginTop': '5%','color':'blue'}),
                #html.Img(src = 'assets/msj.png', style = {'width': '95%', 'height':'70%','text-Align': 'center'}),
                  html.A(html.Img(src = 'assets/msj.png', style = {'width': '95%', 'height':'70%','text-Align': 'center'}),href='http://127.0.0.1:8887/consejo'),
                html.H6('Escucha nuestros consejos sobre como ahorrar, prparate para jubilación, emprendimiento y gastos futuros.',style = { 'margin': 10, 'color': 'black'})
              ]
            )
          ]
        ),
  ])


layout_ahorro=html.Div([
        html.Img(src = 'assets/header1.png', style = {'width': '100%', 'height': 80, 'marginBottom': 15}),
        html.H1("Simulador de Ahorro", style = {'textAlign': 'center', 'fontSize': '40','marginBottom': '5px', 'marginTop': '5%','color':'blue'}),
        html.Div( className='row',  # Define the row element
          children=[
            html.Div(id = 'controls',className='six columns', style = {'backgroundColor': '#C7E7F5', 'marginLeft': 20, 'height': 650, 'borderRadius': '10px'},
              children = [
                html.Iframe(src = "https://creator.us.uneeq.io/try/619d0f46-d845-4249-961f-f634d94613be", style = {"width": '100%', "height": "100%", 'borderRadius': '10px'} )
              ]
            ),
          ]
        )
  ])


#layout_choque=html.Div([html.H1("Simulador de Choque", style = {'textAlign': 'center', 'fontSize': '40','marginBottom': '5px', 'marginTop': '5%','color':'blue'})])
layout_choque=html.Div([
        html.Img(src = 'assets/header1.png', style = {'width': '100%', 'height': 80, 'marginBottom': 15}),
        html.H1("Simulador de Choque", style = {'textAlign': 'center', 'fontSize': '40','marginBottom': '5px', 'marginTop': '5%','color':'blue'}),
        html.Div( className='row',  # Define the row element
          children=[
            html.Div(id = 'controls',className='six columns', style = {'backgroundColor': '#C7E7F5', 'marginLeft': 20, 'height': 650, 'borderRadius': '10px'},
              children = [
                html.Iframe(src = "https://creator.us.uneeq.io/try/619d0f46-d845-4249-961f-f634d94613be", style = {"width": '100%', "height": "100%", 'borderRadius': '10px'} )
              ]
            ),
          ]
        )
  ])
layout_consejo=html.Div([html.H1("Simulador de consejos", style = {'textAlign': 'center', 'fontSize': '40','marginBottom': '5px', 'marginTop': '5%','color':'blue'})])

layout_tips = html.Div([
    html.Img(src = 'assets/header1.png', style = {'width': '100%', 'height': 80, 'marginBottom': 15}),
    html.H1('Consejos',style = {'textAlign': 'center', 'fontSize': '100px','marginBottom': '5px', 'marginTop': '2%','color':'blue'}),
    html.Div([
      html.Ul([
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2017/09/07/08/54/money-2724248__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("1. Define metas financieras", style = {'color': 'black'}),
          html.P("Es muy difícil llegar a un lugar si no sabes a dónde vas. El primer paso para dar un buen manejo a tu dinero es saber qué es lo que quieres lograr con él. Las metas deben ser a corto, mediano y largo plazo.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2017/10/25/19/45/piggy-bank-2889042_1280.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("2. Identifica la totalidad de tus ingresos", style = {'color': 'black'}),
          html.P("Al identificar de dónde provienen tus ingresos podrás asignar un mejor valor a tu tiempo, de forma que le podrás dedicar especial atención a las actividades que te hacen obtener dinero.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2016/10/09/19/19/coins-1726618_1280.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("3. Haz una lista con todos tus gastos", style = {'color': 'black'}),
          html.P("Hacer una lista de todos tus gastos es uno de los puntos más importantes, pues te ayuda a darte cuenta en qué estás gastando tu dinero y cuánto estás gastando. Si te cuesta trabajo, puedes ayudarte de la tecnología, pues existen aplicaciones móviles para anotar tus gastos.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2017/09/07/08/54/money-2724241_1280.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("4. Divide tus gastos en fijos y variables", style = {'color': 'black'}),
          html.P("Hacer una lista de todos tus gastos es uno de los puntos más importantes, pues te ayuda a darte cuenta en qué estás gastando tu dinero y cuánto estás gastando. Si te cuesta trabajo, puedes ayudarte de la tecnología, pues existen aplicaciones móviles para anotar tus gastos. ", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2014/12/21/23/57/money-576443__480.png", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("5. Usa herramientas", style = {'color': 'black'}),
          html.P("Desde un cuaderno hasta una aplicación móvil, lo importante es registrar tus finanzas en algún lugar donde puedas visualizar y llevar un control de tus gastos", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),

        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2015/10/31/08/50/coins-1015125__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("6. Plantéate eliminar la mayor cantidad de gastos variables que puedas", style = {'color': 'black'}),
          html.P("Los gastos variables son aquellos que no son necesarios para subsistir. Para disminuirlos debes eliminar los que no retribuyen positivamente en tu vida.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2014/11/08/18/23/credit-squeeze-522549__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("7. Analiza si tienes un balance positivo al final del mes", style = {'color': 'black'}),
          html.P("Un balance positivo es que al final del mes, tus gastos no sean mayores o iguales que tus ingresos. Para saber qué tipo de balance tienes, resta la totalidad de tus gastos (fijos y variables) a tus ingresos. Si tienes dinero sobrante, es positivo. Si no tienes sobrante o te endeudas, es negativo. ", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2016/06/01/08/40/money-1428594__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("8. Prioriza la totalidad de tus gastos", style = {'color': 'black'}),
          html.P("Tus gastos deben priorizarse y jerarquizarse. Por ejemplo, nunca debes dejar de pagar tus gastos fijos por usar el dinero en tus gastos variables. De entre tus gastos variables, hay algunos que son más necesarios que otros. ", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img( src="https://cdn.pixabay.com/photo/2016/12/06/04/17/money-1885540__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("9. Haz un presupuesto mensual alineado con tus metas", style = {'color': 'black'}),
          html.P("Un presupuesto es la guía que debe dictar cómo gastar tu dinero y te dirá con precisión con cuánto dispones para cada día y para cada actividad. Alinear tu presupuesto mensual con tus metas, te permitirá trazar un camino más preciso para conseguirlas. ", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2016/03/05/20/00/accountant-1238598__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("10. Establece tus límites y aprende a decirte “no me alcanza”", style = {'color': 'black'}),
          html.P("Si algún gasto o actividad se sale de tu presupuesto, evítalo por completo. La importancia de decir “no me alcanza”, radica en saber con precisión cuáles son los gastos innecesarios que se salen de tu presupuesto.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2015/10/02/10/09/piggy-bank-968302__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("11. Crea un fondo de emergencias y prevé riesgos", style = {'color': 'black'}),
          html.P("Las emergencias pueden deshacer todas tus acciones para cuidar tu dinero. La mejor forma es prepararse para ellas. Si bien es cierto que es imposible, saber lo que va a pasar, puedes hacer un fondo que se use cuando una emergencia así lo requiera.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img( src="https://cdn.pixabay.com/photo/2017/09/26/16/08/savings-2789112__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("12. Identifica tus deudas", style = {'color': 'black'}),
          html.P("Las deudas son deberes financieros que debes cubrir en tiempo y forma de manera que no causen daños serios a tu salud financiera. Para identificarlas, debes escribir en qué consiste cada una de esas obligaciones, de forma que estés preparado para cumplir con ellas.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2015/08/01/21/03/euro-870757__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("13. Prioriza tus deudas", style = {'color': 'black'}),
          html.P("Una buena forma de priorizar es por la fecha en la que se deben cumplir, otra forma es priorizar aquellas que tendrán peores consecuencias al no cubrirlas y otra forma es por aquellas que se pueden cubrir con mayor facilidad.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2017/03/19/18/49/auto-financing-2157347__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("14. Analiza adquirir deudas que trabajen a tu favor", style = {'color': 'black'}),
          html.P("Endeudarte para obtener rendimientos te permite capitalizar una deuda. Es importante que analices bien antes de empezar una acción como esta, pues debes estar seguro de que tu inversión será redituable.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2016/08/15/17/38/piggy-bank-1595992__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("15. No te endeudes para cubrir otras deudas", style = {'color': 'black'}),
          html.P("Si ya tienes deudas, adquirir nuevas para pagar las viejas no es la mejor idea. Es cierto que existen métodos de consolidación o refinanciación, pero lo cierto es que deben ser las últimas opciones y deben estar acompañadas de un buen análisis de las implicaciones.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2017/09/07/08/53/money-2724238__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("16. No te sobre endeudes", style = {'color': 'black'}),
          html.P("Lo ideal es no endeudarse más allá de lo que se puede pagar. Sin embargo, es bastante común sobre endeudarse pensando que se puede cumplir con esas obligaciones. Debes mantener las deudas controladas y usar las opciones de crédito a tu favor. ", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img( src="https://cdn.pixabay.com/photo/2016/10/07/07/33/save-1720971__480.jpg",width="300", height="200" ,style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("17. Analiza los meses sin intereses", style = {'color': 'black'}),
          html.P("Los meses sin intereses son grandiosas formas de comprar sin pagar más por lo que se adquiere. Sin embargo, se debe tener precaución de las condiciones en las que se adquiere un plan de esta naturaleza o la cantidad de estos planes con los que se puede cumplir al mismo tiempo.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2017/09/07/08/54/money-2724248__480.jpg", width="300", height="200",style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("18. Evita los excesos", style = {'color': 'black'}),
          html.P("En la vida, ningún exceso es bueno. Cuando se trata de finanzas personales la regla se aplica con la misma fuerza. No gastes de más; no te endeudes de más, busca siempre alcanzar un buen balance en la vida y en tu salud financiera.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2015/08/01/21/03/euro-870757__480.jpg", width="300", height="200" ,style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("19. Cuidado con los gastos “hormiga”", style = {'color': 'black'}),
          html.P("Los gastos hormiga, son aquellos que no representan un gran desembolso en un inicio, pero la suma de ellos hace que se conviertan en una gran fuga de dinero. Se deben identificar, pues son muy complicados de erradicar. ", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2017/09/26/16/08/savings-2789112__480.jpg", width="300", height="200" ,style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("20. Evita las compras por impulso", style = {'color': 'black'}),
          html.P("Comprar por impulso es muy peligroso. Las compras por impulso se parecen a los gastos hormigas debido a que se realizan cuando se adquieren productos innecesarios. La diferencia es que, generalmente, son productos más caros y no tardarás en darte cuenta de que no lo necesitabas.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2018/03/15/22/40/fraud-3229757__480.jpg", width="300", height="200" ,style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("21. Distingue entre los caprichos y las necesidades", style = {'color': 'black'}),
          html.P("Para evitar las compras por impulso o los gastos innecesarios, debemos tener muy claro cuáles son los caprichos y cuáles son las necesidades. ", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img( src="https://cdn.pixabay.com/photo/2020/06/14/22/33/investment-5299600__480.jpg", width="300", height="200" ,style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("22. Compra sólo lo necesario", style = {'color': 'black'}),
          html.P("Para evitar gastar de más y salirse del presupuesto la recomendación pasa por sólo comprar lo necesario y planificar las compras.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img( src="https://cdn.pixabay.com/photo/2016/09/29/17/05/hourglass-1703349__480.jpg", width="300", height="200" ,style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("23. Hazlo tú mismo", style = {'color': 'black'}),
          html.P("Si haces las reparaciones de tu hogar puedes no gastar de más y ahorrar. Evidentemente si se requiere algo con mucha especialización, deberías contratar a un especialista.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img(src="https://cdn.pixabay.com/photo/2015/07/18/18/14/piggy-bank-850607__480.jpg", width="300", height="200" ,style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("24. Habla de tus estrategias financieras y escucha las de los demás ", style = {'color': 'black'}),
          html.P("Compartir tus estrategias financieras es una muy buena forma de obtener otras ideas que complementen las acciones que ya se están llevando a cabo.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),
        html.Li([
          html.Img( src="https://cdn.pixabay.com/photo/2015/09/20/18/31/coins-948603__480.jpg", width="300", height="200" ,style={'float': 'left','margin': '0 15px 0 0'}),
          html.H1("25. Pagar los impuestos", style = {'color': 'black'}),
          html.P("Recuerda que debes estar al corriente con el pago de impuestos. Asegúrate de reservar suficiente dinero para pagar y de que puedas hacerlo antes de la fecha límite. Esto te ahorrará dinero.", style={  'font':  '400 18px/1.5 Georgia', 'color': 'black'})
        ], style={'padding': '10px', 'overflow': 'auto'}),

      ],style={'list-style-type': 'none', 'width': '100%', 'backgroundColor': '#C7E7F5', 'borderRadius': '10px'})
    ],style={ 'margin': '20px'})


  ])


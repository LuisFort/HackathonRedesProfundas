import flask
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from layouts import layout_dashboard, login_form
import callbacks
from app import appDash


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
	
	if pathname == '/dashboard':
		return layout_dashboard

	if pathname == '/login':
		return login_form
	
	else:	
		return html.H1('404', style = {'textAlign': 'center', 'fontSize': '40'})
			
	

# ------------------------------------------------------------------------------
if __name__ == '__main__':
	appDash.run_server(debug=True)
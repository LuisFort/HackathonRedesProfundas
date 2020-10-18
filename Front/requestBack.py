import requests
import json
import pandas as pd

#urlGeneral = 'http://0.0.0.0:1018/'
urlGeneral = 'https://api.lago-de-datos.ga/v1/'

def rLogin(mail, password) :
	url = urlGeneral + 'login'
	data = {'mail': mail, 'password': password}
	response = requests.post(url, data = data)


	if int(response.status_code) == 200 :
		res = json.loads(response.text)
		print(res)

		return res

	return None

def rRefresh(refresh_token):
	
	headers = {'Authorization': 'Bearer ' + refresh_token}
	url = urlGeneral + 'refresh'
	response = requests.post(url, headers = headers)

	print(response.status_code)
	if int(response.status_code) == 200 :
		res = json.loads(response.text)
		print(res)
		return res['access_token']

	return None

def rInfo(access_token, refresh_token, mes, sexo, gen, minS, maxS) :
	
	headers = {'Authorization': 'Bearer ' + access_token}
	url = urlGeneral + 'info'
	data = {'sexo': sexo, 'mes': mes, 'generacion': gen, 'sueldo_minimo': minS, 'sueldo_maximo': maxS}
	response = requests.post(url, data = data, headers = headers)
	print('hola')
	print(response.status_code)
	
	if int(response.status_code) == 200 :
		res = json.loads(response.text)
		print('hola2')
		estados = []
		personas = []
		print(res['data'])
		for key in res['data'] :
			if key != 'Distrito Federal' :
				estados.append(key)
				personas.append(res['data'][key])

		df = pd.DataFrame({'Estado': estados, 'Personas': personas})
		
		return df, res['avg_edades'], res['avg_sueldos'], access_token, refresh_token, False

	elif int(response.status_code) == 401 :
		new_access_token = rRefresh(refresh_token)
		if new_access_token :
			headers = {'Authorization': 'Bearer ' + new_access_token}
			response = requests.post(url, data = data, headers = headers)
			print('que pedo')
			if int(response.status_code) == 200 :
				res = json.loads(response.text)
				print(res['data'])
				estados = []
				personas = []
				for key in res['data'] :
					if key != 'Distrito Federal' :
						estados.append(key)
						personas.append(res['data'][key])

				df = pd.DataFrame({'Estado': estados, 'Personas': personas})

				return df, res['avg_edades'], res['avg_sueldos'], new_access_token, refresh_token, True
			else :
				None, None, None, None , None, None
		else :
			return None, None, None, None, None, None

def rInfoMunicipio(access_token, refresh_token, estado, mes, sexo, gen, minS, maxS) :
	
	headers = {'Authorization': 'Bearer ' + access_token}
	url = urlGeneral + 'infoMunicipios'
	data = {'estado': estado, 'sexo': sexo, 'mes': mes, 'generacion': gen, 'sueldo_minimo': minS, 'sueldo_maximo': maxS}
	response = requests.post(url, data = data, headers = headers)
	print('Entre a lo de municipios')
	print(response.status_code, response.text)
	if int(response.status_code) == 200 :
		res = json.loads(response.text)
		municipios = []
		personas = []
		print(res['data'])
		for key in res['data'] :
			
			municipios.append(key)
			personas.append(res['data'][key])

		df = pd.DataFrame({'Municipio': municipios, 'Personas': personas})
		
		return df, res['avg_edades'], res['avg_sueldos'], access_token, refresh_token, False

	elif int(response.status_code) == 401 :
		print('Entre en municipios en el 401')
		new_access_token = rRefresh(refresh_token)
		if new_access_token :
			headers = {'Authorization': 'Bearer ' + new_access_token}
			response = requests.post(url, data = data, headers = headers)
			print('que pedo en municipios')
			if int(response.status_code) == 200 :
				res = json.loads(response.text)
				print(res['data'])
				municipios = []
				personas = []
				for key in res['data'] :
					municipios.append(key)
					personas.append(res['data'][key])

				df = pd.DataFrame({'Municipio': municipios, 'Personas': personas})

				return df, res['avg_edades'], res['avg_sueldos'], new_access_token, refresh_token, True
			else :
				None, None, None, None , None, None
		else :
			return None, None, None, None, None, None

import os, time, pytz
os.environ['TZ'] = 'America/Mexico_City'
time.tzset()
tz = pytz.timezone("America/Mexico_City") 
from dotenv import load_dotenv
load_dotenv()
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
passwd = os.getenv('DB_PASS')
database = os.getenv('DB_NAME')
secret_key = os.getenv('JWT_SECRET_KEY')

from passlib.apps import custom_app_context as pwd_context
from flask_jwt_extended import (
	JWTManager, jwt_required, create_access_token,
	jwt_refresh_token_required, create_refresh_token,
	get_jwt_identity, get_raw_jwt, decode_token
)
from flask import Flask ,request, jsonify, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import mysql.connector
import datetime


# initialization
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ user + ':' + passwd + '@' + host + '/' + database 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['JWT_SECRET_KEY'] = secret_key

jwt = JWTManager(app)

# extensions
db = SQLAlchemy(app)


CORS(app)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#MODELOS DE LA BASE

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	mail = db.Column(db.String(150))
	password_hash = db.Column(db.String(128))
	edad = db.Column(db.String(10)) 
	genero = db.Column(db.String(30))
	created_at = db.Column(db.DateTime(), default=datetime.datetime.now(tz))
	updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now(tz), default=datetime.datetime.now(tz))	

	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)



class Token(db.Model):
	__tablename__ = 'tokens'
	id = db.Column(db.Integer, primary_key=True)
	mail = db.Column(db.String(150))
	aToken = db.Column(db.String(500))
	rToken = db.Column(db.String(500))
	status = db.Column(db.Boolean())
	created_at = db.Column(db.DateTime(), default=datetime.datetime.now(tz))
	updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now(tz), default=datetime.datetime.now(tz))




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
	


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ENDPOINTS DE ACCESO Y CREACION DE USUARIOS

@app.route('/users', methods=['POST'])
def new_user():
	
	try :
		data = request.get_json(force=True)
		print(data)
		with open("logs_data.txt", "a+") as f:
				f.write("this is data: " + str(data)+'\n')
		password = data['password']
		mail = data['mail']
		edad = data['edad']
		genero = data['genero']
		
	except :
		return jsonify({'status': 'failed', 'msg': 'missing arguments'}),400

	

	if mail is None or password is None or edad is None or genero is None:
		return (jsonify({'status': 'failed', 'msg': 'missing arguments'}),400)	# missing arguments
	if User.query.filter_by(mail=mail).first() is not None:
		return (jsonify({'status': 'failed', 'msg': 'User exists'}),400)	# existing user
	

	try :
		user = User(mail = mail, edad = edad, genero = genero, created_at = datetime.datetime.now(tz), updated_at = datetime.datetime.now(tz))
		user.hash_password(password)
		db.session.add(user)
		db.session.commit()
		
		
		
	except TypeError :
		return jsonify({'status': 'failed', 'msg': 'Invalid value for sex'}),400

	return jsonify({'status': 'success', 'msg': 'user created'}), 201
				





@app.route('/login', methods=['POST'])
def login():
   
	#data = request.form
	data = request.get_json(force=True)
	print(data)
	with open("logs_data.txt", "a+") as f:
			f.write("this is data: " + str(data)+'\n')
	mail = data['mail']
	password = data['password']
		
	user = User.query.filter_by(mail=mail).first()
	if not user or not user.verify_password(password):
		return jsonify({"msg": "Wrong mail or password", "status": "failed"}), 400
	
	
	time_acces = datetime.timedelta(seconds=600) #cambiar a 600 segundos cuando se implemente el dashboard
	time_refresh = datetime.timedelta(days=10) 
	access_token = create_access_token(identity={'mail': mail}, expires_delta=time_acces)
	refresh_token = create_refresh_token(identity={'mail': mail}, expires_delta=time_refresh)
	ret = {
		'access_token': access_token,
		'refresh_token': refresh_token
	}
	atoken_decode = decode_token(access_token)
	rtoken_decode = decode_token(refresh_token)

	
	token = Token(mail=mail, aToken=atoken_decode['jti'], rToken=rtoken_decode['jti'], status=1, created_at = datetime.datetime.now(tz), updated_at = datetime.datetime.now(tz))
	db.session.add(token)
	db.session.commit()
	
	return jsonify(ret), 200



@app.route('/logout', methods=['POST'])
@jwt_required
def logout():
	current_user = get_jwt_identity()
	atoken_decode = get_raw_jwt()['jti']
	verify_status_user = db.session.query(Token.id, Token.status).filter_by(aToken=atoken_decode).first()
	if verify_status_user :
		db.session.query(Token).filter(Token.mail == current_user['mail'], Token.aToken == atoken_decode).update({Token.status: 0, Token.updated_at: datetime.datetime.now(tz)})
		db.session.commit()
		

	return jsonify({"msg": "Successfully logged out", "status": "success"}), 200

	

@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
   
	current_user = get_jwt_identity()
	
	rtoken_decode = get_raw_jwt()['jti']
	
	verify_status_user = db.session.query(Token.id, Token.status).filter_by(rToken=rtoken_decode).first()
	
	if verify_status_user and verify_status_user[1]  :
		time_acces = datetime.timedelta(seconds=600) #cambiar a 600 cuando se active el dashboard
		access_token = create_access_token(identity=current_user, expires_delta=time_acces)
		ret = {
			'access_token': access_token
		}
		atoken_decode = decode_token(access_token)

		db.session.query(Token).filter(Token.mail == current_user['mail'], Token.rToken == rtoken_decode).update({Token.aToken: atoken_decode['jti'], Token.updated_at: datetime.datetime.now(tz)})
		db.session.commit()

		return jsonify(ret), 200
	else :
		return jsonify({'msg':'Session has expired', "status": "failed"}), 401

@app.route('/prueba', methods=['GET'])
def hola():
	return jsonify({'message': 'hola'}), 200

@app.route('/getUser', methods=['GET'])
@jwt_required
def getUser():
	mail = request.args.get('mail')
	userId = db.session.query(User.id).filter_by(mail = mail).first()
	if userId :
		return jsonify({'id': userId[0], 'status': 'success'}), 200
	return jsonify({'message': 'User not found', 'status': 'failed'}),400




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
	if not os.path.exists('db.sqlite'):
		db.create_all()
	app.run(host= '0.0.0.0', debug = False, port = 9876)
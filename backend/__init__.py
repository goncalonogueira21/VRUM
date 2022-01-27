
from socket import SocketIO
from flask import Flask, request, Response, jsonify ,make_response
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
#from flask.ext.cors import cross_origin

from secretsFolder import secrets
import datetime


# cors = CORS()

app = Flask(__name__)

CORS_ALLOW_ORIGIN="*,*"
CORS_EXPOSE_HEADERS="*,*"
CORS_ALLOW_HEADERS="content-type,*"
#cors = CORS(app, origins=CORS_ALLOW_ORIGIN.split(","), allow_headers=CORS_ALLOW_HEADERS.split(",") , expose_headers= CORS_EXPOSE_HEADERS.split(","),   supports_credentials = True)

cors = CORS(app,resources={r"/*":{"origins":"*"}})

socketio = SocketIO(app, cors_allowed_origins="*")
#socketio.run(app)
#DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH = os.path.join(os.getcwd(),"private_key.txt")
#DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH = os.path.join(os.getcwd(),"public_key.txt")

#VAPID_PRIVATE_KEY = open(DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
#VAPID_PUBLIC_KEY = open(DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH, "r+").read().strip("\n")

#VAPID_CLAIMS = {
#"sub": "mailto:develop@raturi.in"
#}




#cors.init_app(app)

#socketio = SocketIO(app)


conn = "mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8mb4".format(secrets.dbuser, secrets.dbpass, secrets.dbhost,
                                                                secrets.dbname)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
# database name
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# SQLAlchemy instance
db = SQLAlchemy(app)


from utilizadores import auth_blueprint
from carros import carro_blueprint
from pedidos import pedido_blueprint
from viagens import viagem_blueprint
from avaliacoes import avaliacao_blueprint
from notificacao import notificacao_blueprint
from mensagens import mensagem_blueprint


app.register_blueprint(auth_blueprint, url_prefix='/utilizador')
app.register_blueprint(carro_blueprint, url_prefix='/carro')
app.register_blueprint(pedido_blueprint, url_prefix='/pedido')
app.register_blueprint(viagem_blueprint, url_prefix='/viagem')
app.register_blueprint(avaliacao_blueprint, url_prefix='/avaliacao')
app.register_blueprint(mensagem_blueprint, url_prefix='/mensagem')
app.register_blueprint(notificacao_blueprint, url_prefix='/notificacao')
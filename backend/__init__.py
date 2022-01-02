from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from secretsFolder import secrets

# cors = CORS()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.debug = True

cors.init_app(app)

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


app.register_blueprint(auth_blueprint, url_prefix='/utilizador')
app.register_blueprint(carro_blueprint, url_prefix='/carro')
app.register_blueprint(pedido_blueprint, url_prefix='/pedido')
app.register_blueprint(viagem_blueprint, url_prefix='/viagem')
app.register_blueprint(avaliacao_blueprint, url_prefix='/avaliacao')

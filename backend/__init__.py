from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from secretsFolder import secrets

#cors = CORS()

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

from views import auth_blueprint
app.register_blueprint(auth_blueprint)

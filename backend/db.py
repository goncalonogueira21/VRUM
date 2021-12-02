from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
import jwt
import pymysql


from functools import wraps

# configuration
from backend.app import app
from backend.venv import secrets

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app.config['SECRET_KEY'] = 'SECRET KEY'
# database name
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# creates SQLALCHEMY object
db = SQLAlchemy(app)

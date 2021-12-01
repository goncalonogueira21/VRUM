from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)

# Colocar uma secret key
app.secret_key = 'colocar secret key'

# Info da DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'TODO'
app.config['MYSQL_DB'] = 'TODO'

# Intialize MySQL
mysql = MySQL(app)

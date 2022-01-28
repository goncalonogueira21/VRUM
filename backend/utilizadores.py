import sys
from typing import ByteString
import jwt
from functools import wraps
from flask import request, jsonify, make_response, Blueprint
from flask_socketio import join_room
from sqlalchemy.dialects.mysql import base
from sqlalchemy.sql.expression import null
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import text
from datetime import datetime, timedelta
from flask_cors import cross_origin
import base64


import json


auth_blueprint = Blueprint('auth_blueprint', __name__)

from __init__ import db, app, socketio
from models import Utilizador


# TODO: Delete and Update

@auth_blueprint.route('/')
def testdb():
    try:
        print(db.session.query(text('show tables')))  # .from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # see Terminal for description of the error
        print("\nThe error:\n" + str(e) + "\n")
        return '<h1>Something is broken.</h1>'


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256", options={"verify_exp": False})
            current_user = Utilizador.query \
                .filter_by(username=data['username']) \
                .first()
        except:
            return jsonify({
                'message': 'Token is invalid!'
            }), 401
        # returns the current logged in users context to the routes
        return f(*args, **kwargs)

    return decorated

#obter todos os utilizadores
@auth_blueprint.route('/todos', methods=['GET'])
#@token_required
def get_all_users():
    # querying the database
    # for all the entries in it
    users = Utilizador.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for user in users:
        # appending the user data json
        # to the response list
        output.append({
            'username': user.username,
            # 'name': user.name,
            'email': user.email,
            'password': user.password
        })

    response = jsonify({'Utilizadores': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# route for logging user in
@auth_blueprint.route('/login', methods=['POST'])
def login():
    # creates dictionary of form data
    #auth = request.form
    auth = json.loads(request.data)

    if not auth or not auth['username'] or not auth['password']:
        # returns 401 if any username or / and password is missing
        return make_response(
            'Não foi possível verificar o username',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required!"'}
        )

    user = Utilizador.query \
        .filter_by(username=auth['username']) \
        .first()


    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Utilizador não existe',
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist!"'}
        )

    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(minutes=720)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return make_response({'token': token}, 201)

    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'}
    )


#para testar as imagens
@auth_blueprint.route('/testeImagem', methods=['POST'])
@cross_origin()
def registar2():
    # creates a dictionary of the form data
        data=request.form
        texto=data.get('avatar')
        avatar=base64.b64decode(texto)
        #foto = "".join(["{:08b}".format(x) for x in foto1])
        avatarencoded=base64.b64encode(avatar)
        #PARA TIRAR O B E AS PELICAS
        final = str(avatarencoded, 'UTF-8')
        print(final)
        #fotoencoded=base64.b64encode(ByteString)
        
        return make_response('E TASS', 201)
    
@auth_blueprint.route('/registo', methods=['POST'])
@cross_origin()
def registar():
    db.session.rollback()
    # creates a dictionary of the form data
    data = request.form

    # gets name, email and password
    username, email = data.get('username'), data.get('email')
    password = data.get('password')
    firstname=data.get('firstName')
    lastname=data.get('lastName')
    telemovel=data.get('nrTelemovel')
    morad=data.get('morada')
    nascimento=data.get('dataNascimento')
    about=data.get('aboutME')
    if data.get('avatar'):
        avatar= base64.b64decode(data.get('avatar'))
    else:
        avatar = base64.b64decode('')
    # checking for existing user
    user = Utilizador.query \
        .filter_by(username=username) \
        .first()
    if not user:
        # database ORM object
        user = Utilizador(
            username=username,
            email=email,
            password=generate_password_hash(password),
            firstName=firstname,
            lastName=lastname,
            nrTelemovel=telemovel,
            rating=0,
            morada=morad,
            dataNascimento=nascimento,
            aboutME=about,
            avatar=avatar
        )
        # insert user
        db.session.add(user)
        db.session.commit()

        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)

#get user info by username
@auth_blueprint.route('/<string:id>', methods=['GET'])
@cross_origin()
def get(id):
    user = Utilizador.query.filter_by(username=id).first()
    output = []
    if request.method == 'GET':
        if user:
            if (user.avatar) : 
                ava = str(base64.b64encode(user.avatar),'UTF-8')
            else : 
               ava = ''
            output.append({
                'username': user.username,
                'firstName': user.firstName,
                'lastName': user.lastName,
                'email': user.email,
                'nrTelemovel': user.nrTelemovel,
                'rating': user.rating,
                'morada': user.morada,
                'dataNascimento': str(user.dataNascimento),
                'aboutME': user.aboutME,
                'avatar':  ava
        
            })
            return make_response(jsonify(output), 200)
    return make_response('Utilizador não existe', 204)




# Eliminar um utilizador
@auth_blueprint.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    user = Utilizador.query.filter_by(username=id).first()
    if request.method == 'POST':
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response('Utilizador removido com sucesso.', 200)
 
    return make_response('Utilizador não existe', 204)



#Editar utilizador
@auth_blueprint.route('/<string:id>/update', methods=['PUT'])
@token_required
def updateUser(id):
    user = Utilizador.query.get(id)
    token = request.headers['Authorization']
    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256", options={"verify_exp": False})
    if not data['username'] == id:
        return make_response('You can not do that', 404)
    if user is not None:
        data=request.form

        for d in data:
            #session.execute(update(stuff_table, values={stuff_table.c.foo: stuff_table.c.foo + 1}))
            if(d=='avatar'):
                #imagens pequenas
                avatar = base64.b64decode(data.get(d))
                setattr(user,d,avatar)
            elif(d=='dataNascimento'):
                days = data.get(d)
                if "-" not in days:
                    setattr(user,d,datetime.strptime(data.get(d),"%d/%m/%Y"))
                else:
                    setattr(user, d, datetime.strptime(data.get(d), "%Y-%m-%d"))
            else:
                setattr(user,d,data.get(d))
            
        
        db.session.commit()
        

        

        return make_response('User atualizado com sucesso', 200)
    else:
        return make_response('User nao existe', 404)

#quando se faz login
@socketio.on("connection")
def connect_handler(msg):
    print(msg)
    user_room = 'user_' + msg
    print("USER ROOM É :" + user_room)
    join_room(user_room)
    print("o zat?")
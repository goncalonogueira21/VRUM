from mailbox import Mailbox
from flask import Blueprint, jsonify, make_response, request
from sqlalchemy import text, Date, or_, and_
from datetime import date
from datetime import datetime as dt


mensagem_blueprint = Blueprint('mensagem_blueprint', __name__)

from __init__ import db, app
from models import Mensagem, mailbox
from utilizadores import token_required


# GET Obter todas as Mensagens
@mensagem_blueprint.route('/todas', methods=['GET'])
@token_required
def get_all_mensagens():
    # querying the database
    # for all the entries in it
    mensagens=Mensagem.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    
    for m in mensagens:

        output.append({
            'idMensagem': m.idMensagem,
            'conteudo': m.conteudo,
            'userOrigem': m.userOrigem,
            'userDestino': m.userDestino,
            'data': dt.strftime(m.dataInicio, '%Y-%m-%d %H:%M'),
        })

    response = jsonify({'Mensagens': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



# GET Obter todas as mensagens de dois utilizadores
@mensagem_blueprint.route('/<string:id1>&<string:id2>', methods=['GET'])
@token_required
def get_all_users_mensagens(id1, id2):
    # querying the database
    # for all the entries in it
    mensagens=Mensagem.query.filter((and_(Mensagem.userOrigem==id1 ,Mensagem.userDestino==id2)) | (and_(Mensagem.userOrigem==id2 ,Mensagem.userDestino==id1))  ) 
                        

    

    # converting the query objects  
    # to list of jsons
    output = []
    for mensagem in mensagens:
        # appending the user data json
        # to the response list
        
        if mensagem.userOrigem == id1 and mensagem.userDestino == id2:
            output.append({
                #'idMensagem': mensagem.idMensagem,
                'content': mensagem.conteudo,
                #'userOrigem' : mensagem.userOrigem,
                #'userDestino': mensagem.userDestino,
                'created_at': mensagem.data,
                'me': 1

            })
        else:
            output.append({
                'content': mensagem.conteudo,
                'created_at': mensagem.data,
                'me': 0
            })
        
    
    response = jsonify({'Mensagens': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# GET Obter mailbox de um utilizador
@mensagem_blueprint.route('/mailbox/<string:id>', methods=['GET'])
@token_required
def get_mailbox(id):
    # querying the database
    # for all the entries in it
    mail=mailbox.query.filter(or_(mailbox.fk_Utilizador_username==id, mailbox.fk_Utilizador_username2==id)).all()

    # converting the query objects
    # to list of jsons
    output = []
    count=1
    active= 'false'
    for line in mail:
        # appending the user data json
        # to the response list
        if (count==1):
            active = 'true'
        if (line.fk_Utilizador_username== id):
            output.append({
                #'fk_Utilizador_username': line.fk_Utilizador_username,
                'id': count,
                'title': line.fk_Utilizador_username2,
                'active' : active
            })
            break
        if(line.fk_Utilizador_username2== id):
            output.append({
                #'fk_Utilizador_username': line.fk_Utilizador_username,
                'id': count,
                'title': line.fk_Utilizador_username,
                'active' : active
            })
            break
        count+=1

    response = jsonify({'Mailbox': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# POST Regista uma mensagem
@mensagem_blueprint.route('/registo', methods=['POST'])
@token_required
def registar_mensagem():
    # creates a dictionary of the form data
    data = request.form

    # gets all attributes
    conteudo = data.get('content')
    userOrigem = data.get('userOrigem')
    userDestino = data.get('userDestino')
    created_at = data.get('created_at')
    

    # database ORM object
    mensagem = Mensagem(
        conteudo = conteudo,
        userOrigem = userOrigem,
        userDestino = userDestino,
        data = created_at,
    )

    # Verifica se existe um par entre os users na bd da mailbox
    mail=mailbox.query.filter_by(fk_Utilizador_username=userOrigem, fk_Utilizador_username2=userDestino).first()
    if not mail:
        line = mailbox(
            fk_Utilizador_username=userOrigem,
            fk_Utilizador_username2=userDestino,
            mailbox=0
        )
        db.session.add(line)


    # insert mensagem
    db.session.add(mensagem)
    db.session.commit()

    return make_response('Mensagem Enviada.', 201)

#POST Regista um mailbox
@mensagem_blueprint.route('/registoMailBox', methods=['POST'])
@token_required
def registar_mailBox():
    # creates a dictionary of the form data
    data = request.form

    # gets all attributes
    userOrigem = data.get('userorigem')
    userDestino = data.get('userdestino')
    # Verifica se existe um par entre os users na bd da mailbox
    mail=mailbox.query.filter_by(fk_Utilizador_username=userOrigem,fk_Utilizador_username2=userDestino).first()
    if not mail:
        line = mailbox(
            fk_Utilizador_username=userOrigem,
            fk_Utilizador_username2=userDestino,
            mailbox=0
        )
        db.session.add(line)
        db.session.commit()

        return make_response('mailBox Criada',200)


    else : return make_response('Já existe mailbox', 201)
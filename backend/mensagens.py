from dataclasses import dataclass
from flask import Blueprint, jsonify, make_response, request
from sqlalchemy import text, Date, and_
from datetime import date
from datetime import datetime as dt


mensagem_blueprint = Blueprint('mensagem_blueprint', __name__)

from __init__ import db, app
from models import Mensagem, MailBox

# GET Obter todas as Mensagens
@mensagem_blueprint.route('/todas', methods=['GET'])
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

# GET Obter todas as mensagens de um utilizador
@mensagem_blueprint.route('/<string:id>', methods=['GET'])
def get_all_user_mensagens(id):
    # querying the database
    # for all the entries in it
    mensagens=Mensagem.query.filter(Mensagem.userOrigem==id, Mensagem.userDestino==id)

    # converting the query objects
    # to list of jsons
    output = []
    for mensagem in mensagens:
        # appending the user data json
        # to the response list
        output.append({
            'idMensagem': mensagem.idMensagem,
            'conteudo': mensagem.conteudo,
            'userOrigem' : mensagem.userOrigem,
            'userDestino': mensagem.userDestino,
            'data': mensagem.data,

        })

    response = jsonify({'Mensagens': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# GET Obter todas as mensagens de dois utilizadores
@mensagem_blueprint.route('/<string:id1>&<string:id2>', methods=['GET'])
def get_all_users_mensagens(id1, id2):
    # querying the database
    # for all the entries in it
    mensagens=Mensagem.query.filter((Mensagem.userOrigem==id1, Mensagem.userDestino==id2) | (Mensagem.userOrigem==id2, Mensagem.userDestino==id1))


    # converting the query objects
    # to list of jsons
    output = []
    for mensagem in mensagens:
        # appending the user data json
        # to the response list
        output.append({
            'idMensagem': mensagem.idMensagem,
            'conteudo': mensagem.conteudo,
            'userOrigem' : mensagem.userOrigem,
            'userDestino': mensagem.userDestino,
            'data': mensagem.data,

        })

    response = jsonify({'Mensagens': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# GET Obter mailbox de um utilizador
@mensagem_blueprint.route('/<string:id>', methods=['GET'])
def get_mailbox(id):
    # querying the database
    # for all the entries in it
    mailbox=MailBox.query.filter(MailBox.fk_Utilizador_username==id, MailBox.fk_Utilizador_username2==id)

    # converting the query objects
    # to list of jsons
    output = []
    for line in mailbox:
        # appending the user data json
        # to the response list
        output.append({
            'fk_Utilizador_username': line.fk_Utilizador_username,
            'fk_Utilizador_username2': line.fk_Utilizador_username2,
            'mailbox' : line.mailbox,

        })

    response = jsonify({'Mailbox': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# POST Regista uma mensagem
@mensagem_blueprint.route('/registo', methods=['POST'])
def registar_mensagem():
    # creates a dictionary of the form data
    data = request.form

    # gets all attributes
    conteudo = data.get('conteudo')
    userOrigem = data.get('userOrigem')
    userDestino = data.get('userDestino')
    dataM = date.today()
    

    # database ORM object
    mensagem = Mensagem(
        conteudo = conteudo,
        userOrigem = userOrigem,
        userDestino = userDestino,
        data = dataM,
    )

    # Verifica se existe um par entre os users na bd da mailbox
    mailbox=MailBox.query.filter(MailBox.fk_Utilizador_username==userOrigem, MailBox.fk_Utilizador_username2==userDestino)
    if mailbox.count() == 0:
        line = MailBox(
            fk_Utilizador_username=userOrigem,
            fk_Utilizador_username2=userDestino,
            mailbox=0
        )
        db.session.add(line)


    # insert mensagem
    db.session.add(mensagem)
    db.session.commit()

    return make_response('Mensagem Enviada.', 201)


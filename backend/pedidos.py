import re
from flask import Blueprint, jsonify, request, make_response
from sqlalchemy import text
from sqlalchemy.orm import session
from werkzeug.wrappers import response


pedido_blueprint = Blueprint('pedido_blueprint', __name__)

from __init__ import db, app
from models import Pedido

#Obter os pedidos todos
@pedido_blueprint.route('/todos', methods=['GET'])
def get_all_pedidos():
    # querying the database
    # for all the entries in it
    pedidos=Pedido.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for pedido in pedidos:
        # appending the user data json
        # to the response list
        output.append({
            'id': pedido.idPedido,
            'username': pedido.fk_Utilizador_username,
            # 'name': user.name,
            'viagem': pedido.fk_Viagem_idViagem,
            'nrPessoas': pedido.nrPessoas,
            'pickupLocal': pedido.pickupLocal,
            'destino':pedido.localDestino,
            'aceite':pedido.aceite,
        })

    response = jsonify({'Pedidos': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

#Obter um pedido em especifico
@pedido_blueprint.route('/<int:id>', methods=['GET'])
def getPedido(id):
     pedido=Pedido.query.get(id)
     if not pedido:
        return make_response('Pedido nao existe', 404)
     else:
         output=[]
        
         output.append({
            'id': pedido.idPedido,
            'username': pedido.fk_Utilizador_username,
            # 'name': user.name,
            'viagem': pedido.fk_Viagem_idViagem,
            'nrPessoas': pedido.nrPessoas,
            'pickupLocal': pedido.pickupLocal,
            'destino':pedido.localDestino,
            'aceite':pedido.aceite,
        })
         response= jsonify({'Pedido': output})
         response.headers.add("Access-Control-Allow-Origin", "*")
         return response


#Registar um pedido
#Esta a dar merda
@pedido_blueprint.route('/registo', methods=['POST'])
def registar():
    # creates a dictionary of the form data
    db.session.rollback()
    data = request.form

    # gets all attributes
    fk_Utilizador_username, fk_Viagem_idViagem = data.get('fk_Utilizador_username'), data.get('fk_Viagem_idViagem')
    nrPessoas, pickupLocal = data.get('nrPessoas'), data.get('pickupLocal')
    localDestino = data.get('localDestino')
    # checking for existing pedido
    pedido = Pedido.query \
        .filter_by(fk_Utilizador_username=fk_Utilizador_username, fk_Viagem_idViagem = fk_Viagem_idViagem) \
        .first()
    if not pedido:
        # database ORM object
        pedido = Pedido(
            fk_Utilizador_username=fk_Utilizador_username,
            fk_Viagem_idViagem=fk_Viagem_idViagem,
            nrPessoas=nrPessoas,
            pickupLocal=pickupLocal,
            localDestino=localDestino,
            aceite=0
        )
        # insert user
        db.session.add(pedido)
        db.session.commit()

        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('Ja fizeste um pedido nesta viagem.', 202)

#Eliminar pedido
@pedido_blueprint.route('/<int:idpedido>/remove', methods=['Delete'])
def eliminarPedido(idpedido):
    print ('its working--Delete group')
    if Pedido.query.filter_by(idPedido=idpedido).first() is not None:
        Pedido.query.filter_by(idpedido=idpedido).delete()
        db.session.commit()
        return make_response('Pedido removido com sucesso.', 200)
    else:
        return make_response('Pedido nao existe', 204)


#Atualizar pedido
#esta a dar merda
@pedido_blueprint.route('/<int:idpedido>/update', methods=['Put'])
def updatePedido(idpedido):

    pedido = Pedido.query.get(idpedido)
    print(pedido)

    if pedido is not None:
        data=request.form

    

        for d in data:
            #session.execute(update(stuff_table, values={stuff_table.c.foo: stuff_table.c.foo + 1}))
            setattr(pedido,d,data.get(d))
            
        
        db.session.commit()
        

        

        return make_response('Pedido atualizado com sucesso', 200)
    else:
        return make_response('Pedido nao existe', 404)
        
    

    
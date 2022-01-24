import re
from flask import Blueprint, jsonify, request, make_response
from sqlalchemy import text,and_
from sqlalchemy.orm import session
from werkzeug.wrappers import response


pedido_blueprint = Blueprint('pedido_blueprint', __name__)

from __init__ import db, app
from models import Pedido, Viagem, Usufrui

# GET Obter os pedidos todos
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
            'estado':pedido.estado,
            #'notificacao':pedido.estado
        })

    response = jsonify({'Pedidos': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# GET Obter um pedido em especifico
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
            'estado':pedido.estado,
            #'notificacao':pedido.notificacao
        })
         response= jsonify({'Pedido': output})
         response.headers.add("Access-Control-Allow-Origin", "*")
         return response


# POST Registar um pedido
@pedido_blueprint.route('/registo', methods=['POST'])
def registar():
    # creates a dictionary of the form data
    db.session.rollback()
    data = request.form
    # gets all attributes
    fk_Utilizador_username, fk_Viagem_idViagem = data.get('username'), data.get('idViagem')
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
            estado="Pedido Enviado",
            #notificacao=1,
        )
        # insert user
        db.session.add(pedido)
        db.session.commit()

        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('Ja fizeste um pedido nesta viagem.', 202)

# DELETE Eliminar pedido
@pedido_blueprint.route('/<int:idpedido>/remove', methods=['Delete'])
def eliminarPedido(idpedido):
    print ('its working--Delete group')
    if Pedido.query.filter_by(idPedido=idpedido).first() is not None:
        Pedido.query.filter_by(idPedido=idpedido).delete()
        db.session.commit()
        return make_response('Pedido removido com sucesso.', 200)
    else:
        return make_response('Pedido nao existe', 204)


# PUT Atualizar pedido
@pedido_blueprint.route('/<int:idpedido>/update', methods=['Put'])
def updatePedido(idpedido):

    pedido = Pedido.query.get(idpedido)

    if pedido is not None:
        data=request.form

    

        for d in data:
            #session.execute(update(stuff_table, values={stuff_table.c.foo: stuff_table.c.foo + 1}))
            setattr(pedido,d,data.get(d))
            
        
        db.session.commit()
        

        

        return make_response('Pedido atualizado com sucesso', 200)
    else:
        return make_response('Pedido nao existe', 404)
        
    
# GET Todos os pedidos recebidos de um utilizador
@pedido_blueprint.route('todos/recebido/<string:idCondutor>', methods=['GET'])
def getAllpedidosRecebidos(idCondutor):

    output = []

    result = db.session.query(Viagem, Pedido).filter(and_(Viagem.idCondutor == idCondutor, Viagem.idViagem==Pedido.fk_Viagem_idViagem)).all()

    for r,s in result:

         output.append({
             'idPedido': s.idPedido,
             'username': s.fk_Utilizador_username,
             'viagem': s. fk_Viagem_idViagem,
             'pickupLocal': s.pickupLocal,
             'localDestino' :s.localDestino,
             'nrPessoas': s.nrPessoas,
             'estado': s.estado,
             'idPedido': s.idPedido,
             'data': r.dataInicio,
             #'notificacao':s.notificacao
         })

    
    response = jsonify({'Recebido': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# GET Todos os pedidos POR ACEITAR recebidos de um utilizador 
@pedido_blueprint.route('todos/recebidoAceitar/<string:idCondutor>', methods=['GET'])
def getAllpedidosRecebidos_porAceitar(idCondutor):

    output = []

    result = db.session.query(Viagem, Pedido).filter(and_(Viagem.idCondutor == idCondutor, Viagem.idViagem==Pedido.fk_Viagem_idViagem)).all()

    for r,s in result:
        if s.estado == "Pedido Enviado":
            output.append({
                'username': s.fk_Utilizador_username,
                'viagem': s. fk_Viagem_idViagem,
                'pickupLocal': s.pickupLocal,
                'localDestino' :s.localDestino,
                'nrPessoas': s.nrPessoas,
                'estado': s.estado,
                'idPedido': s.idPedido
            })
    
    response = jsonify({'Recebido': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

#notificaçoes de pedidos recebidos
@pedido_blueprint.route('todos/recebido/notificacao/<string:idCondutor>', methods=['GET'])
def getAllnotificacoesRecebidas(idCondutor):

    output = []

    result = db.session.query(Viagem, Pedido).filter(and_(Viagem.idCondutor == idCondutor, Viagem.idViagem==Pedido.fk_Viagem_idViagem)).all()

    for r,s in result:

         output.append({
             'username': s.fk_Utilizador_username,
             'viagem': s. fk_Viagem_idViagem,
             'pickupLocal': s.pickupLocal,
             'localDestino' :s.localDestino,
             'nrPessoas': s.nrPessoas,
             'estado': s.estado,
             #'notificacao':s.notificacao
         })

    
    response = jsonify({'RecebidoNotificacao': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

    

# GET Todos os pedidos enviados de um utilizador
@pedido_blueprint.route('todos/enviado/<string:idPassageiro>', methods=['GET'])
def getAllPedidosEnviados(idPassageiro):

    pedidos=Pedido.query.filter(Pedido.fk_Utilizador_username==idPassageiro)

    # converting the query objects
    # to list of jsons
    output = []

    for pedido in pedidos:
        # appending the user data json
        # to the response list
        output.append({
            'idPedido': pedido.idPedido,
            'fk_Utilizador_username': pedido.fk_Utilizador_username,
            'fk_Viagem_idViagem' : pedido.fk_Viagem_idViagem,
            'nrPessoas': pedido.nrPessoas,
            'pickupLocal': pedido.pickupLocal,
            'localDestino': pedido.localDestino,
            'estado': pedido.estado
        })


    response = jsonify({'Pedidos': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@pedido_blueprint.route('todos/enviado/notificacao/<string:idPassageiro>', methods=['GET'])
def getAllnotificacoesEnviados(idPassageiro):

    output = []

    pedido=Pedido.query.filter_by(fk_Utilizador_username=idPassageiro,notificacao=1).first()
    
    if not pedido:
        return make_response('Pedido nao existe', 200)
    else:
        viagem= Viagem.query.get(pedido.fk_Viagem_idViagem)
        
        output.append({
            'id': pedido.idPedido,
            'viagem': pedido.fk_Viagem_idViagem,
            'nrPessoas': pedido.nrPessoas,
            'pickupLocal': pedido.pickupLocal,
            'localDestino':pedido.localDestino,
            'estado':pedido.estado,
            #'notificacao':pedido.notificacao,
            'data': viagem.dataInicio
        })

        response= jsonify({'EnviadoNotificacao': output})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
  

# PUT Aceita Pedido
@pedido_blueprint.route('/<int:idpedido>/aceitar', methods=['Put'])
def aceitaPedido(idpedido):


    pedido = Pedido.query.get(idpedido)
    print("IDentificador do pedido" , pedido.idPedido)
    #mudar na tabela pedidos,
    setattr(pedido,"estado","Aceite")
    #setattr(pedido,"notificacao", 1)
    custo = Viagem.query.get(pedido.fk_Viagem_idViagem).custoPessoa
    #inserir entrada na tabela "usufrui"
    usufrui = Usufrui(
        fk_Utilizador_username= pedido.fk_Utilizador_username,
        fk_Viagem_idViagem=pedido.fk_Viagem_idViagem,
        custoPago= custo
    )
    db.session.add(usufrui)
    db.session.commit()




    return make_response('Alteracao bem sucedida', 200)

# PUT Elimina Viagens nos Pedidos
@pedido_blueprint.route('/<int:idpedido>/eliminar', methods=['Put'])
def eliminaViagemPedido(idpedido):


    pedido = Pedido.query.get(idpedido)
    print("IDentificador do pedido" , pedido.idPedido)
    #mudar na tabela pedidos,
    setattr(pedido,"estado","Eliminada")
    #setattr(pedido,"notificacao", 1)
    db.session.commit()




    return make_response('Alteracao bem sucedida', 200)
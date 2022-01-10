from sqlalchemy.sql.sqltypes import DateTime
from flask import Blueprint, jsonify, make_response, request
from sqlalchemy.sql import text, and_
from datetime import datetime


viagem_blueprint = Blueprint('viagem_blueprint', __name__)

from __init__ import db, app
from models import Viagem

#Obter as Viagens todas
@viagem_blueprint.route('/todos', methods=['GET'])
def get_all_viagens():
    # querying the database
    # for all the entries in it
    viagens=Viagem.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for viagem in viagens:
        # appending the user data json
        # to the response list
        output.append({
            'id': viagem.idViagem,
            'username': viagem.fk_Carro_matricula,
            # 'name': user.name,
            'dataInicio': viagem.dataInicio,
            'kmsViagem': viagem.kmsViagem,
            'custoPessoa': viagem.custoPessoa,
            'localInicio':viagem.localInicio,
            'bagagem':viagem.bagagem,
            'localDestino': viagem.localDestino,
            'nrLugares': viagem.nrLugares,
            'lugaresDisp': viagem.lugaresDisp,
            'regularidade': viagem.regularidade,
            'idCondutor': viagem.idCondutor,
            'descricao': viagem.descricao,
            'estado': viagem.estado,
        })

    response = jsonify({'Viagens': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response




#ViagemComFiltros
#é preciso passar o intervalo de tempo pela querystring e os outros atributos pelo body
@viagem_blueprint.route('/filtros', methods=['GET'])
def get_viagens_filtros():
    # querying the database
    # for all the entries in it

    
    #form
    data = request.form
    #queryString
    arg = request.args
    #if data.get('desde') or ('ate'):
    #    print("o zataoooo")
    
    if (arg):
        if (arg.get('dataInicio') and arg.get('dataFim')):
            
            inicio=arg.get('dataInicio')
            fim = arg.get('dataFim')
            viagens=Viagem.query.filter(and_(Viagem.dataInicio >= inicio , Viagem.dataInicio <= fim)).filter_by(**data)
                   
        elif (arg.get('dataFim')):
            fim=arg.get('dataFim')
            viagens=Viagem.query.filter(Viagem.dataInicio <= fim).filter_by(**data)
        else:
            inicio = arg.get('dataInicio')
            viagens=Viagem.query.filter(Viagem.dataInicio >= inicio ).filter_by(**data)
            
    
    else: 
        ##se nao tiver comparacoes gt ou assim
        viagens=Viagem.query.filter_by(**data)

        # converting the query objects
        # to list of jsons
    output = []
    for viagem in viagens:
        # appending the user data json
        # to the response list
        output.append({
            'id': viagem.idViagem,
            'username': viagem.fk_Carro_matricula,
            # 'name': user.name,
            'dataInicio': viagem.dataInicio,
            'kmsViagem': viagem.kmsViagem,
            'custoPessoa': viagem.custoPessoa,
            'localInicio':viagem.localInicio,
            'bagaem':viagem.bagagem,
            'localDestino': viagem.localDestino,
            'nrLugares': viagem.nrLugares,
            'lugaresDisp': viagem.lugaresDisp,
            'regularidade': viagem.regularidade,
            'idCondutor': viagem.idCondutor,
            'descricao': viagem.descricao
        })

    response = jsonify({'Viagens': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


#Obter as Viagens todas de um utilizador condutor
@viagem_blueprint.route('/todos/:id', methods=['GET'])
def get_all_viagens_condutor(id):
    # querying the database
    # for all the entries in it
    viagens=Viagem.query.all()
    # converting the query objects
    # to list of jsons

    output = []
    for viagem in viagens:
        # appending the user data json
        # to the response list

        if (viagem.idCondutor == id):
            output.append({
            'id': viagem.idViagem,
            'username': viagem.fk_Carro_matricula,
            # 'name': user.name,
            'dataInicio': viagem.dataInicio,
            'kmsViagem': viagem.kmsViagem,
            'custoPessoa': viagem.custoPessoa,
            'localInicio':viagem.localInicio,
            'bagagem':viagem.bagagem,
            'localDestino': viagem.localDestino,
            'nrLugares': viagem.nrLugares,
            'lugaresDisp': viagem.lugaresDisp,
            'regularidade': viagem.regularidade,
            'idCondutor': viagem.idCondutor,
            'descricao': viagem.descricao,
            'estado': viagem.estado,
        })      
    response = jsonify({'Viagem': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

#Obter uma Viagem em especifico
@viagem_blueprint.route('/<int:id>', methods=['GET'])
def getViagem(id):
     viagem=Viagem.query.get(id)
     if not viagem:
        return make_response('Pedido nao existe', 404)
     else:
         output=[]
        
         output.append({
            'id': viagem.idViagem,
            'username': viagem.fk_Carro_matricula,
            # 'name': user.name,
            'dataInicio': viagem.dataInicio,
            'kmsViagem': viagem.kmsViagem,
            'custoPessoa': viagem.custoPessoa,
            'localInicio':viagem.localInicio,
            'bagagem':viagem.bagagem,
            'localDestino': viagem.localDestino,
            'nrLugares': viagem.nrLugares,
            'lugaresDisp': viagem.lugaresDisp,
            'regularidade': viagem.regularidade,
            'idCondutor': viagem.idCondutor,
            'descricao': viagem.descricao,
            'estado': viagem.estado,
        })
         response= jsonify({'Viagem': output})
         response.headers.add("Access-Control-Allow-Origin", "*")
         return response





#Registar uma viagem
@viagem_blueprint.route('/registo', methods=['POST'])
def registar():
    # creates a dictionary of the form data
    data = request.form

    # gets all attributes
    matricula= data.get('fk_Carro_matricula')
    inicio, kms = data.get('dataInicio'), data.get('kmsViagem')
    custoP, localIni = data.get('custoPessoa'), data.get('localInicio')
    bagag, localDest= data.get('bagagem'), data.get('localDestino')
    lugaresDisp, reg = data.get('lugaresDisp'), data.get('regularidade')
    idCond , desc = data.get('idCondutor'), data.get('descricao')
    nrLugares=(data.get('nrLugares'))
    # checking for existing viagem (ver qual a restricao)
    viagem = Viagem.query \
        .filter_by(idCondutor=idCond) \
        .first()
    if not viagem:
        # database ORM object
        viagem = Viagem(
            fk_Carro_matricula=matricula,
            dataInicio=inicio,
            kmsViagem=kms,
            custoPessoa=custoP,
            localInicio=localIni,
            bagagem=bagag,
            localDestino=localDest,
            nrLugares=nrLugares,
            lugaresDisp=lugaresDisp,
            regularidade=reg,
            idCondutor=idCond,
            descricao=desc,
            estado='Agendada'
        )
        # insert user
        db.session.add(viagem)
        db.session.commit()

    # checking for existing viagem (ver qual a restricao)
    # viagem = Viagem.query \
    #     .filter_by(idCondutor=idCond) \
    #     .first()
    
    # if not viagem:
        # database ORM object
    viagem = Viagem(
        fk_Carro_matricula=matricula,
        dataInicio=inicio,
        kmsViagem=kms,
        custoPessoa=custoP,
        localInicio=localIni,
        bagagem=bagag,
        localDestino=localDest,
        lugaresDisp=lugaresDisp,
        regularidade=reg,
        idCondutor=idCond,
        descricao=desc,
        estado='Agendada',
        nrLugares=0 # TODO: Ir buscar nr de lugares do carro
    )
    # insert user
    print("Viagem ", viagem)
    db.session.add(viagem)
    db.session.commit()

    return make_response('Successfully registered.', 201)
    # else:
    #     # returns 202 if user already exists
    #     return make_response('Esta viagem ja existe.', 202)

#Eliminar Viagem
@viagem_blueprint.route('/<int:idviagem>/remove', methods=['Delete'])
def eliminarPedido(idviagem):
    print ('its working--Delete group')
    if Viagem.query.filter_by(idViagem=idviagem).first() is not None:
        Viagem.query.filter_by(idViagem=idviagem).delete()
        db.session.commit()
        return make_response('Viagem removida com sucesso.', 200)
    else:
        return make_response('Viagem nao existe', 204)


#Atualizar pedido
#esta a dar merda
@viagem_blueprint.route('/<int:idviagem>/update', methods=['Put'])
def updateViagem(idviagem):

    viagem = Viagem.query.get(idviagem)
    print(viagem)

    if viagem is not None:
        data=request.form

    

        for d in data:
            #session.execute(update(stuff_table, values={stuff_table.c.foo: stuff_table.c.foo + 1}))
            setattr(viagem,d,data.get(d))
            
        
        db.session.commit()
        

        

        return make_response('Pedido atualizado com sucesso', 200)
    else:
        return make_response('Pedido nao existe', 404)
        
    

    

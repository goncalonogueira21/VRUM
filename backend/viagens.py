from sqlalchemy.sql.sqltypes import DateTime
from flask import Blueprint, jsonify, make_response, request
from sqlalchemy.sql import text, and_ , func
from datetime import datetime as dt


viagem_blueprint = Blueprint('viagem_blueprint', __name__)

from __init__ import db, app
from models import Viagem, Usufrui

# GET Obter as Viagens todas
@viagem_blueprint.route('/todos', methods=['GET'])
def get_all_viagens():
    # querying the database
    # for all the entries in it
    viagens=Viagem.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for viagem in viagens:
        if (viagem.estado != 'Finalizada'):
        # appending the user data json
        # to the response list
            output.append({
                'id': viagem.idViagem,
                'username': viagem.fk_Carro_matricula,
                # 'name': user.name,
                'dataInicio': dt.strftime(viagem.dataInicio, '%Y-%m-%d'),
                'horaInicio': dt.strftime(viagem.dataInicio, '%H:%M'),
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


# GET Lista de Viagens Disponíveis
@viagem_blueprint.route('/disponiveis', methods=['GET'])
def get_disponiveis_viagens():
    # querying the database
    # for all the entries in it
    viagens=Viagem.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for viagem in viagens:
        if (viagem.estado == 'Agendada'):
        # appending the user data json
        # to the response list
            output.append({
                'id': viagem.idViagem,
                'username': viagem.fk_Carro_matricula,
                # 'name': user.name,
                'dataInicio': dt.strftime(viagem.dataInicio, '%Y-%m-%d'),
                'horaInicio': dt.strftime(viagem.dataInicio, '%H:%M'),
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





# GET ViagemComFiltros
#é preciso passar o intervalo de tempo pela querystring e os outros atributos pelo body
@viagem_blueprint.route('/filtros', methods=['Post'])
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
            'dataInicio': dt.strftime(viagem.dataInicio, '%Y-%m-%d'),
            'horaInicio': dt.strftime(viagem.dataInicio, '%H:%M'),
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


# GET Obter as Viagens todas de um utilizador condutor
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
            'dataInicio': dt.strftime(viagem.dataInicio, '%Y-%m-%d'),
            'horaInicio': dt.strftime(viagem.dataInicio, '%H:%M'),
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

# GET Obter uma Viagem em especifico
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
            'dataInicio': dt.strftime(viagem.dataInicio, '%Y-%m-%d'),
            'horaInicio': dt.strftime(viagem.dataInicio, '%H:%M'),
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





# POST Registar uma viagem
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
    horaInicio = data.get('horaInicio')
    horaCombinada =dt.strptime( inicio + " " + horaInicio, '%Y-%m-%d %H:%M')
    #nrLugares=(data.get('nrLugares'))
    # checking for existing viagem (ver qual a restricao)
    viagem = Viagem.query \
        .filter_by(idCondutor=idCond) \
        .filter_by(dataInicio=horaCombinada) \
        .first()
    if not viagem:
        # database ORM object
        
    # if not viagem:
        # database ORM object
        viagem = Viagem(
            fk_Carro_matricula=matricula,
            dataInicio=horaCombinada,
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
    
    else:
        
        return make_response('Esta viagem ja existe.', 202)

# DELETE Eliminar Viagem
@viagem_blueprint.route('/<int:idviagem>/remove', methods=['Delete'])
def eliminarPedido(idviagem):
    print ('its working--Delete group')
    if Viagem.query.filter_by(idViagem=idviagem).first() is not None:
        Viagem.query.filter_by(idViagem=idviagem).delete()

        # TODO: Mudar o estado dos pedidos desta viagem para "Eliminada" e eliminar as entradas na tabela usufrui
        db.session.commit()
        return make_response('Viagem removida com sucesso.', 200)
    else:
        return make_response('Viagem nao existe', 204)


# PUT Atualizar viagem
@viagem_blueprint.route('/<int:idviagem>/update', methods=['Put'])
def updateViagem(idviagem):

    viagem = Viagem.query.get(idviagem)

    if viagem is not None:
        data=request.form

        for d in data:
            #session.execute(update(stuff_table, values={stuff_table.c.foo: stuff_table.c.foo + 1}))
            setattr(viagem,d,data.get(d))         
        
        db.session.commit()

        return make_response('Viagem atualizado com sucesso', 200)
    else:
        return make_response('Viagem nao existe', 404)
        
    
# GET Lista de viagens de um Passageiro
@viagem_blueprint.route('/todos/passageiro/<string:idPassageiro>', methods=['GET'])
def get_all_viagens_passageirocustos(idPassageiro):
    # querying the database
    # for all the entries in it
    output = []

    result = db.session.query(Usufrui, Viagem).filter(and_(Usufrui.fk_Utilizador_username == idPassageiro, Usufrui.fk_Viagem_idViagem==Viagem.idViagem,Viagem.estado == 'Finalizada')).all()
    for r,s in result:

        output.append({
            'idViagem': r.fk_Viagem_idViagem,
            'matricula': s.fk_Carro_matricula,
            'condutor': s.idCondutor,
            'dataInicio': dt.strftime(s.dataInicio, '%Y-%m-%d'),
            'localInicio':s.localInicio,
            'localDestino': s.localDestino,
            'custo' : r.custoPago 
        })

    response = jsonify({'Viagem': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# GET Lista de Viagens de um Condutor
@viagem_blueprint.route('/todos/condutor/<string:idDriver>', methods=['GET'])
def get_all_viagens_condutor_custos(idDriver):
    # querying the database
    # for all the entries in it
    viagens=Viagem.query.filter_by(idCondutor=idDriver, estado='Finalizada')

    output = []
    for viagem in viagens:
        # appending the user data json
        # to the response list

        custos=db.session.query(func.sum(Usufrui.custoPago).label("custoPago")).filter_by(fk_Viagem_idViagem=viagem.idViagem).first()


        #print("Valor ganho: " ,custos.custoPago)
        
        output.append({
            'id': viagem.idViagem,
            'matricula': viagem.fk_Carro_matricula,
            # 'name': user.name,
            'dataInicio': dt.strftime(viagem.dataInicio, '%Y-%m-%d'),
            'localInicio':viagem.localInicio,
            'localDestino': viagem.localDestino,
            #'custoGanho' : "{:.2f}".format(custos.custoPago) 
        })  
    response = jsonify({'Viagem': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# GET Lista de passageiros de uma viagem
@viagem_blueprint.route('/passageiros/<string:idViagem>', methods=['GET'])
def get_passageiros_viagem(idViagem):
    # querying the database
    # for all the entries in it
    output = []

    tabela=Usufrui.query.filter_by(fk_Viagem_idViagem=idViagem)
    for linha in tabela:

        output.append({
            'idViagem': linha.fk_Viagem_idViagem,
            'fk_Utilizador_username': linha.fk_Utilizador_username,
            'custoPago': linha.custoPago

        })

    response = jsonify({'Passageiros': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
from flask import Blueprint, jsonify, make_response, request
from sqlalchemy.sql import text

viagem_blueprint = Blueprint('viagem_blueprint', __name__)

from __init__ import db, app
from models import Viagem

#TODO

@viagem_blueprint.route('/')
def testdb():
    try:
        
        print(db.session.query(text('show tables')))  # .from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # see Terminal for description of the error
        print("\nThe error:\n" + str(e) + "\n")
        return '<h1>Something is broken.</h1>'


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
            'bagaem':viagem.bagagem,
            'localDestino': viagem.localDestino,
            'nrLugares': viagem.nrLugares,
            'lugaresDisp': viagem.lugaresDisp,
            'regularidade': viagem.regularidade,
            'idCondutor': viagem.idCondutor,
            'descricao': viagem.descricao
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
    lugarDisp, reg = data.get('lugaresDisp'), data.get('regularidade')
    idCond , desc = data.get('idCondutor'), data.get('descricao')
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
            nrLugares=lugarDisp,
            regularidade=reg,
            idCondutor=idCond,
            descricao=desc
        )
        # insert user
        db.session.add(viagem)
        db.session.commit()

        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('Esta viagem ja existe.', 202)

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
        
    

    

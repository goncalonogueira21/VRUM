from dataclasses import dataclass
from flask import Blueprint, jsonify, make_response, request
from sqlalchemy import text, Date, and_
from datetime import date


avaliacao_blueprint = Blueprint('avaliacao_blueprint', __name__)

from __init__ import db, app
from models import Avaliacao, Utilizador, Viagem

#Regista a avaliação do condutor de uma determinada viagem
@avaliacao_blueprint.route('/<int:id>', methods=['POST'])
def rate_user(id):

    new_score = request.form.get("rating")
    current_user = request.form.get("username")
    viagem = Viagem.query.get(id)
    id_condutor = viagem.idCondutor
    user = Utilizador.query.get(id_condutor)

    rating = Avaliacao.query.filter((Avaliacao.utilizador==current_user) & (Avaliacao.fk_Viagem_idViagem==id)).first()
    

    if not rating:
        rating = Avaliacao(fk_Viagem_idViagem=id, conteudo=new_score, dataAvaliacao=date.today(), utilizador=current_user)
        
        result = db.session.query(Avaliacao, Viagem).filter(and_(Viagem.idCondutor == id_condutor, Avaliacao.fk_Viagem_idViagem==Viagem.idViagem)).all()

       


        n_avaliacoes = len(result)+1
        r = user.rating
        newrating= (r + int(new_score)) / n_avaliacoes

        setattr(user,'rating',int(newrating))

        db.session.add(rating)
        db.session.commit()

        return make_response('Successfully registered.', 201)
    else :
        return make_response({'Rating': rating.conteudo}, 200)


# GET Avaliação
@avaliacao_blueprint.route('/<string:idViagem>&<string:idUser>', methods=['GET'])
def get_avaliacao(idViagem, idUser):
    # querying the database
    # for all the entries in it

    output = []

    avaliacao=Avaliacao.query.filter_by(fk_Viagem_idViagem=idViagem, utilizador=idUser).first()

    output.append({
            'idAvaliacao': avaliacao.idAvaliacao,
            'utilizador': avaliacao.utilizador,
            'conteudo': avaliacao.conteudo,
            'fk_Viagem_idViagem': avaliacao.fk_Viagem_idViagem,

        })

    response = jsonify({'Avaliação': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
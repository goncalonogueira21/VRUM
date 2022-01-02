from flask import Blueprint, jsonify, make_response, request
from sqlalchemy import text, Date


avaliacao_blueprint = Blueprint('avaliacao_blueprint', __name__)

from __init__ import db, app
from models import Avaliacao, Utilizador, Viagem

#TODO

@avaliacao_blueprint.route('/')
def testdb():
    try:
        print(db.session.query(text('show tables')))  # .from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # see Terminal for description of the error
        print("\nThe error:\n" + str(e) + "\n")
        return '<h1>Something is broken.</h1>'		



#Regista a avaliação do condutor de uma determinada viagem
@avaliacao_blueprint.route('/<int:id>', methods=['POST'])
def rate_user():

    new_score = request.form.get("user-rating")
    
    viagem = Viagem.query.get(id)
    id_condutor = viagem.idCondutor
    user = Utilizador.query.get(id_condutor)

    rating = Avaliacao.query.filter((Avaliacao.utilizador==id_condutor) & (Avaliacao.fk_Viagem_idViagem==id)).first()

    if not rating:
        rating = Avaliacao(fk_Viagem_idViagem=id, conteudo=new_score, dataAvalicao=Date.today(), utilizador=id_condutor)
        n_avaliacoes = len(Avaliacao.query.filter_by(condutor=id_condutor)) +1
        r = user.rating
        user.rating = (r + new_score) / n_avaliacoes

    db.session.add(rating)
    db.session.commit()

    return make_response('Successfully registered.', 201)



      

  

from flask.helpers import make_response
from sqlalchemy.sql.sqltypes import Date
from backend.models import Utilizador, Viagem
from flask import Blueprint
from flask.globals import request

avaliacao_blueprint = Blueprint('avaliacao_blueprint', __name__)

from __init__ import db, app
from models import Avaliacao

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



@avaliacao_blueprint.route('/rate', methods=['POST'])
def rate_user(viagem_id):

    new_score = request.form.get("user-rating")
    
    viagem = Viagem.query.get(viagem_id)
    id_condutor = viagem.idCondutor
    user = Utilizador.query.get(id_condutor)

    rating = Avaliacao.query.filter((Avaliacao.utilizador==id_condutor) & (Avaliacao.fk_Viagem_idViagem==viagem_id)).first()

    if not rating:
        rating = Avaliacao(fk_Viagem_idViagem=viagem_id, conteudo=new_score, dataAvalicao=Date.today(), utilizador=id_condutor)
        n_avaliacoes = len(Avaliacao.query.filter_by(condutor=id_condutor)) +1
        r = user.rating
        user.rating = (r + new_score) / n_avaliacoes

    db.session.add(rating)
    db.session.commit()

    return make_response('Successfully registered.', 201)



      

  

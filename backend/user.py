import jwt
import app

from app import db
from flask import request, jsonify, make_response
from functools import wraps


class Utilizador(db.Model):
    username = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    rating = db.Column(db.INT)
    nrTelemovel = db.Column(db.INT)
    dataNascimento = db.Column(db.DateTime)
    morada = db.Column(db.String(255))


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Utilizador.query \
                .filter_by(username=data['username']) \
                .first()
        except:
            return jsonify({
                'message': 'Token is invalid!'
            }), 401
        # returns the current logged in users context to the routes
        return f(current_user, *args, **kwargs)

    return decorated

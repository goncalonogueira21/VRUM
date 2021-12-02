from functools import wraps

import jwt
from flask import jsonify, request

from backend.app import app
from backend.db import db


class Utilizador(db.Model):
    username = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(100))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    rating = db.Column(db.Integer)
    nrTelemovel = db.Column(db.Integer)
    dataNascimento = db.Column(db.Date)
    morada = db.Column(db.String(100))


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

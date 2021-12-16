from __init__ import db

class Utilizador(db.Model):
    # __tablename__ = 'Utilizador'
    username = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    rating = db.Column(db.INT)
    nrTelemovel = db.Column(db.INT)
    dataNascimento = db.Column(db.DateTime)
    morada = db.Column(db.String(255))

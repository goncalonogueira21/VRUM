from __init__ import db


class Utilizador(db.Model):
    # __tablename__ = 'Utilizador'
    username = db.Column(db.String(45), primary_key=True)
    # name = db.Column(db.String(100))
    password = db.Column(db.String(45))
    firstName = db.Column(db.String(45))
    lastName = db.Column(db.String(45))
    email = db.Column(db.String(45))
    nrTelemovel = db.Column(db.String(9))
    rating = db.Column(db.INT)
    morada = db.Column(db.String(45))
    dataNascimento = db.Column(db.DateTime)
    avatar = db.Column(db.VARBINARY(8000))
    aboutME = db.Column(db.String(200))

from app.db import db

class Internetspeed(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    ruc = db.Column(db.String(100))
    idsegment = db.Column(db.String(100))
    idtecnology = db.Column(db.String(100))
    idstate = db.Column(db.String(100))
    speedmin = db.Column(db.String(100))
    speedmax = db.Column(db.String(100))

    def __init__(self, aula, hora_entrada):
        self.aula = aula
        self.hora_entrada = hora_entrada
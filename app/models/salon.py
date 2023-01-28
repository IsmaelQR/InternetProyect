from app.db import db

class Salon(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    aula = db.Column(db.String(100))
    hora_entrada = db.Column(db.Time)

    def __init__(self, aula, hora_entrada):
        self.aula = aula
        self.hora_entrada = hora_entrada
        



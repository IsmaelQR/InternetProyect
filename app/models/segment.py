from app.db import db

class Segment(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, aula, hora_entrada):
        self.aula = aula
        self.hora_entrada = hora_entrada
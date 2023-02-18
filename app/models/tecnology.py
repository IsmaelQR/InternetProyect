from app.db import db

class Tecnology(db.Model):
    id_tecnology=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, id_tecnology, name):
        self.id_tecnology = id_tecnology
        self.name = name
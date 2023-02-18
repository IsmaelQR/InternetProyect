from app.db import db

class State(db.Model):
    id_state=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, id_segment, name):
        self.id_state = id_segment
        self.name = name
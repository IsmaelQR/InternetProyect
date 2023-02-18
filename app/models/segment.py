from app.db import db

class Segment(db.Model):
    id_segment=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, id_segment, name):
        self.id_segment = id_segment
        self.name = name
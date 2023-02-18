from app.db import db

class Company(db.Model):
    ruc=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(100))
    sunatestate = db.Column(db.String(100))

    def __init__(self, ruc, name , sunatestate):
        self.ruc = ruc
        self.name = name
        self.sunatestate = sunatestate
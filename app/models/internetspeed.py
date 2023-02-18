from app.db import db
from app.models import tecnology

class Internetspeed(db.Model):
    id_speed=db.Column(db.Integer,autoincrement=True,primary_key=True)
    ruc = db.Column(db.Integer)
    id_segment = db.Column(db.Integer)
    #db.relationship('Agent', backref='request', \
    #lazy='select')
    id_tecnology = ('Agent', db.ForeignKey('tecnology.id_tecnology'))
    id_state = db.Column(db.Integer)
    speedmin = db.Column(db.Integer)
    speedmax = db.Column(db.Integer)

    def __init__(self, ruc ,id_segment ,id_tecnology,id_state ,speedmin,speedmax ):
        self.ruc=ruc 
        self.id_segment = id_segment 
        self.id_tecnology = id_tecnology
        self.id_state = id_state 
        self.speedmin = speedmin
        self.speedmax = speedmax
        
        
    
    
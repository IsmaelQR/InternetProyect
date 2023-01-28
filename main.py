from app import create_app
from flask_marshmallow import Marshmallow
import json
from flask import render_template,redirect,url_for
from flask import request,jsonify
from app.db import db
from app.models.salon import Salon
from flask_restful import Api, Resource

app=create_app()
ma = Marshmallow(app) #Es una extensión que facilita la 
#serialización de los modelos de la base de datos a JSON y viceversa
api = Api(app) # new

#Schema de salon
class SalonSchema(ma.Schema):
    class Meta:
        fields = ('id', 'aula', 'hora_entrada')
        model =Salon

salon_schema = SalonSchema() 
salon_schema = SalonSchema(many=True)

@app.route('/') #ruta raiz
def index():
    nuevo_salon= Salon.query.all()
    return render_template('index.html', contacts=nuevo_salon)
 
    
@app.route('/salones',methods=['POST']) #ruta raiz
def add_salones(Resource):
    aula=request.json['aula']
    hora_entrada=request.json['hora_entrada']

    nuevo_salon= Salon(aula, hora_entrada)

    db.session.add(nuevo_salon)
    db.session.commit()


    return jsonify({'message':'salon agregado'})

#api.add_resource(add_salones, '/salones')


""" class Test(Resource):
    @classmethod
    def get(cls, id: int):
        test = Salon.query.filter_by(id=id).all()
        #db.session.query()
        #Salon.query.filter_by(id=id).first_or_404()
        if test:
            return salon_schema.dump(test), 200
        return {"message": ("test_test_not_found")}, 404 """




@app.route('/ver-salones',methods=['GET']) #ruta raiz
def get_salones():
    salon = Salon.query.all()
    if salon:
        return salon_schema.dump(salon), 200
    return {"message": ("No hay aulas registradas")}, 404

#Ver por salon
@app.route('/ver-salones/<id>', methods=['GET'])
def get_salones_id(id):
    salon =Salon.query.filter_by(id=id).all()
    if salon:
        return salon_schema.dump(salon), 200
    return {"message": ("Aula no encontrada")}, 404

#api.add_resource(get_salones_id, "/ver-salones/<id>", endpoint='test-api')

@app.route('/salon/<id>', methods=['DELETE'])
def delete_salon(id):

    salon = Salon.query.get(id)
    db.session.delete(salon)
    db.session.commit()
    return {"message": ("Aula eliminada")}, 200

@app.route('/salon-update/<id>', methods=['PUT'])
def update_salon(id):
        
    salon = Salon.query.get(id)
    aula=request.json['aula']
    hora_entrada=request.json['hora_entrada']

    salon.aula = aula
    salon.hora_entrada = hora_entrada
    db.session.commit()

    return {"message": ("Aula Actualizada")}, 200


db.init_app(app)
with app.app_context():
    db.create_all()
    #print("BD conectada!") 

if __name__ == "__main__":
    app.run(debug=True)

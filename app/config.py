import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'esta-es-una-clave-secreta'
    SQLALCHEMY_DATABASE_URI="mysql://root@localhost/bdosc_api_Rest"
    SQLALCHEMY_TRACK_MODIFICATIONS=False



  
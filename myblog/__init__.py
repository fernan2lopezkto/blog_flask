from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import *

app = Flask(__name__)

#Cargar las configuraciones
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

# importar vistas
from myblog.views.auth import auth

app.register_blueprint(auth)

with app.app_context():
    db.create_all()
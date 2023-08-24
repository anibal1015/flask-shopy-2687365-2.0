from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_bootstrap import Bootstrap

#blueprint
from .mi_blueprint import mi_blueprint
from app.productos import productos
#Creacion y configuracion 
app = Flask(__name__)
app.config.from_object(Config) 
bootstrap = Bootstrap(app)

#resgistro de blueprints
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

#crear los objetos de SQLAlchemy y migrate
db = SQLAlchemy(app)
migrate = Migrate(app ,
                  db)

from .models import Producto, Cliente, Venta
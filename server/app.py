from flask import Flask
from server.models import db
from server.controllers.pizza_controller import pizza_bp  

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(pizza_bp) 

    return app

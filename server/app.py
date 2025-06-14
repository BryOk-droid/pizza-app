from flask import Flask
from server.models import db
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

   
    @app.route('/')
    def home():
        return {'message': 'Welcome to the Pizza API'}

    
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app

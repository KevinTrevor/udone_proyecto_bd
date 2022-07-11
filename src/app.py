from flask import Flask, jsonify, request
from models import insert_costumers
from database import setup
from config import config

# Routes
from routes import customer, order

setup.create_tables()

def create_app():
    """Función que crea la aplicación con Blueprints y errores definidos de la REST API de Chikkkins.
    
    Returns:
        Flask: Objeto Flask para correr una aplicación web.
    """
    app = Flask(__name__)

    # Error handlers
    app.register_error_handler(404, page_not_found)

    # Blueprints
    app.register_blueprint(customer, url_prefix='/customers')
    app.register_blueprint(order, url_prefix='/orders')
    return app

def page_not_found(error):
    """Función que, cuando no se detecta una página, envía un Error HTTP 404.
    Returns:
        tuple(String, Int): Retorna un String con una etiqueta HTMl y el número de error. 
    """
    return "<h1>Not found page</h1>", 404

if __name__ == "__main__":
    app = create_app()
    app.config.from_object(config['development'])

    app.run()
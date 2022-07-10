from flask import Flask
import models

def create_app():
    """Función que crea y define los Blueprints de la REST API de Chikkkins.
    
    Returns:
        Flask: Objeto Flask para correr una aplicación web.
    """
    
    
    app = Flask(__name__)

    @app.route('/')
    def main():
        return "<h1> Hello, Python! </h1>"
    
    @app.route('/costumers', methods=['POST'])
    def create_client():
        data = ("29582382", "Kevin", "04127955420", "kevintrevor0905@gmail.com")
        models.insert_costumers(data)
    
    @app.route('/costumers', methods=['PUT'])
    def modify_client():
        pass
    
    return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
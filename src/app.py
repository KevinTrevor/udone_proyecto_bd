from flask import Flask, jsonify, request
from models import insert_costumers

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
    def create_costumer():
        nombre = request.json['name']
        cedula = request.json['cedula']
        email = request.json['email']
        whatsapp = request.json['whatsapp']
        
        data = (cedula, nombre, whatsapp, email)
        
        costumer_id = insert_costumers(data)
        
        if costumer_id:
            return jsonify({'message': 'New costumers added!'})
        return jsonify({'message': 'Internal error!'})
    
    @app.route('/costumers', methods=['PUT'])
    def modify_client():
        pass
    
    return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
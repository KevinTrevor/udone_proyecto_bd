from flask import Blueprint, jsonify, request
from models import CustomerModel

customer = Blueprint('customer_blueprint', __name__)

@customer.route('/', methods= ['POST'])
def create_costumer():
    """Función que permite crear un nuevo cliente en la base de datos.

    Returns:
        Response: Un archivo en formato JSON.
    """
    try:
        data_json = request.json # Recibe el formato JSON de entrada.
        data = (
            data_json['cedula'], 
            data_json['name'], 
            data_json['whatsapp'], 
            data_json['email']
        ) # Creamos una tupla con los valores del formato JSON.
        CustomerModel.insert_costumers(data) # Se usa la tupla para crear un nuevo cliente.

        return jsonify({'message' : 'New customer added successfully!'})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@customer.route('/', methods= ['GET'])
def get_costumers():
    """Función que permite obtener todos los clientes registrados en la base de datos.
    
    Returns:
        Response: Un archivo en formato JSON.
    """
    try:
        customers = CustomerModel.select_all_costumers() # Nos retorna todos las filas registradas.
        
        return jsonify(customers)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@customer.route('/<cedula>', methods= ['PUT'])
def modify_costumer(cedula):
    """Función que permite modificar a un cliente especifico registrado en la base de datos.
    
    Returns:
        Response: Un archivo en formato JSON.
    """
    try:
        data_json = request.json # Recibe el formato JSON de entrada.
        data = (
            data_json['name'], 
            data_json['whatsapp'], 
            data_json['email'], 
            cedula
            )  # Creamos una tupla con los valores del formato JSON.
        CustomerModel.update_costumer(data) # Se usa la tupla para modificar a un cliente.
        
        return jsonify({'message' : 'Customer successfully modified!'})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
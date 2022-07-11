from flask import Blueprint, jsonify

customer = Blueprint('customer_blueprint', __name__)

@customer.route('/', methods= ['POST'])
def create_costumer():
    return jsonify({'message': 'Work in progress...'})

@customer.route('/', methods= ['GET'])
def get_costumers():
    return jsonify({'message': 'Work in progress...'})

@customer.route('/<cedula>', methods= ['PUT'])
def modify_costumer(cedula):
    return jsonify({'message': 'Work in progress...'})
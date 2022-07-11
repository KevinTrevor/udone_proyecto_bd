from flask import Blueprint, jsonify

order = Blueprint('order_blueprint', __name__)

@order.route('/', methods= ['POST'])
def create_order():
    return jsonify({'message': 'Work in progress...'})

@order.route('/<id>/status', methods= ['PATCH'])
def update_order_status(id):
    return jsonify({'message': 'Work in progress...'})

@order.route('/<id>/payment-screenshoot', methods= ['POST'])
def add_order_screenshot(id):
    return jsonify({'message': 'Work in progress...'})

@order.route('/', methods= ['GET'])
def get_orders():
    return jsonify({'message': 'Work in progress...'})
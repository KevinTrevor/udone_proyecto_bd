from datetime import datetime
from flask import Blueprint, jsonify, request
from models import OrderModel
from utils import DateTimeFormat, Money, FileExtension

order = Blueprint('order_blueprint', __name__)

@order.route('/', methods= ['POST'])
def create_order():
    """Función que permite crear un nuevo pedido en la base de datos.

    Returns:
        Response: Un archivo en formato JSON.
    """
    try: 
        data_json = request.json # Recibe el formato JSON de entrada.

        delivery_amount = Money.get_delivery_amount(data_json['municipality']) # Monto del delivery.
        total_amount = Money.get_total_amount(int(data_json['quantity']), delivery_amount) # Monto total.
        actual_datetime = datetime.now() # Fecha y hora actual.
        hour = DateTimeFormat.format_time(actual_datetime) # Hora con formato.
        date = DateTimeFormat.format_date(actual_datetime) # Fecha con formato.
        status = "pending" # Estado del pedido.

        data = (
            data_json['cedula'],
            data_json['quantity'],
            delivery_amount,
            data_json['payment_method'],
            total_amount,
            status,
            date,
            hour, 
            data_json['city'],
            data_json['municipality'],
            data_json['remarks']
        ) # Creamos una tupla con los valores del formato JSON.

        OrderModel.insert_order(data) # Se usa la tupla para crear un nuevo pedido.
        order = OrderModel.select_last_order() # Retorna el pedido recien creado.

        return jsonify(order)
    except Exception as ex:
        return jsonify({'message': str(ex)})

@order.route('/<id>/status', methods= ['PATCH'])
def modify_order_status(id):
    """Función que permite modificar el estado de un pedido específico en la base de datos.

    Returns:
        Response: Un archivo en formato JSON.
    """
    try:
        status = request.json['status'] # Nuevo estado del pedido.
        data = (status, id) # Creamos una tupla con los valores del formato JSON.
        OrderModel.update_order_status(data) # Se usa la tupla para modificar un pedido específico.

        return jsonify({'message' : 'Order successfully modified!'})
    except Exception as ex:
        return jsonify({'message': str(ex)})
    

@order.route('/<id>/payment-screenshot', methods= ['POST'])
def add_order_screenshot(id):
    """Función que permite ingresar la captura de pago de un pedido específico en la base de datos.

    Returns:
        Response: Un archivo en formato JSON.
    """
    try:
        # Se revisa que exista la llave screenshot.
        if 'screenshot' not in request.files: 
            jsonify({'message' : 'No file part!'})
        
        screenshot = request.files['screenshot']

        # Se revisa que se haya seleccionado algún archivo.
        if screenshot.filename == '': 
            jsonify({'message' : 'No selected file!'})
        
        # Se revisa si tiene una extensión permitida (png/jpg). 
        if screenshot and FileExtension.is_allowed_file(screenshot.filename): 
            data = (screenshot.filename, id)
            OrderModel.insert_order_screenshoot(data)

            return jsonify({'message' : 'Order screenshot successfully updated!'})
        return jsonify({'message' : 'Invalid file extension!'})
    except Exception as ex:
        return jsonify({'message': str(ex)})

@order.route('/', methods= ['GET'])
def get_orders():
    try:
        query_parameters = request.args.to_dict()

        return jsonify(query_parameters)
    except Exception as ex:
        return jsonify({'message': str(ex)})
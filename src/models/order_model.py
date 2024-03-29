from database import get_connection
from .entities import Order
from utils import QueryParamsSQL

class OrderModel:

    @classmethod
    def insert_order(self, data):
        """Función que crea un nuevo pedido en la base de datos."""
             
        sql = """INSERT INTO pedidos (cedula, cantidad, monto_delivery, modo_pago, total,
        estado, fecha, hora, ciudad, municipio, observaciones) VALUES(%s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s);"""

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql, data)
                connection.commit()
            
            connection.close()

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_order_status(self, data):
        """Función que modifica el estado de un pedido específico en la base de datos."""

        sql = "UPDATE pedidos SET estado = (%s) WHERE id = (%s)"
        
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql, data)
                connection.commit()

            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def insert_order_screenshoot(self, data):
        """Función que inserta la captura del pago de un pedido específico en la base de datos."""
        
        sql = "UPDATE pedidos SET screenshot = (%s) WHERE id = (%s)"
        
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql, data)
                connection.commit()

            connection.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def select_order_by_query_params(self, data):

        sql = str(QueryParamsSQL.get_sql_query(data))
        new_data = QueryParamsSQL.get_data_parsed(data)

        print(sql)
        
        try: 
            connection = get_connection()
            orders = []

            with connection.cursor() as cursor:
                if new_data == ():
                    cursor.execute(sql)
                else:
                    cursor.execute(sql, new_data)
                result = cursor.fetchall()
                
                for row in result:
                    order = Order(
                    row[0], 
                    row[1], 
                    row[2], 
                    row[3],
                    row[4], 
                    row[5], 
                    row[6], 
                    row[7],
                    row[8], 
                    row[9], 
                    row[10], 
                    row[11],
                    row[12]
                    )
                    orders.append(order.to_JSON())

            connection.close()
            return orders
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def select_last_order(self):
        """Función que selecciona el último pedido registrado en la base de datos"""

        sql = "SELECT * FROM pedidos ORDER BY id DESC LIMIT 1"

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql)
                row = cursor.fetchone()
                
                order = Order(
                    row[0], 
                    row[1], 
                    row[2], 
                    row[3],
                    row[4], 
                    row[5], 
                    row[6], 
                    row[7],
                    row[8], 
                    row[9], 
                    row[10], 
                    row[11],
                    row[12]
                    )

            connection.close()

            return order.to_JSON()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def select_order_by_id(self, id):
        """Función que selecciona un pedido específico registrado en la base de datos"""

        sql = "SELECT * FROM pedidos WHERE id = (%s)"

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql, (id, ))
                row = cursor.fetchone()
                
                order = Order(
                    row[0], 
                    row[1], 
                    row[2], 
                    row[3],
                    row[4], 
                    row[5], 
                    row[6], 
                    row[7],
                    row[8], 
                    row[9], 
                    row[10], 
                    row[11],
                    row[12]
                    )

            connection.close()

            return order.to_JSON()
        except Exception as ex:
            print("El error esta en select_order_by_id()")
            raise Exception(ex)
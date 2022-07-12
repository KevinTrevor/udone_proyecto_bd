from database import get_connection
from .entities import Customer

class CustomerModel:

    @classmethod
    def insert_costumers(self, data):
        """Función que crea un nuevo cliente en la base de datos."""
             
        sql = "INSERT INTO cliente (cedula, nombre, whatsapp, email) VALUES(%s, %s, %s, %s);"

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql, data)
                connection.commit()
            
            connection.close()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def select_all_costumers(self):
        """Función que selecciona a todos los clientes registrados en la base de datos"""

        sql = "SELECT * FROM cliente ORDER BY cedula ASC"

        try:
            connection = get_connection()
            customers = []

            with connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                
                for row in result:
                    customer = Customer(row[0], row[1], row[2], row[3])
                    customers.append(customer.to_JSON())

            connection.close()
            return customers
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_costumer(self, data):
        """Función que modifica los datos de un cliente registrado en la base de datos"""

        sql = "UPDATE cliente SET nombre = (%s), whatsapp = (%s), email = (%s) WHERE cedula = (%s)"

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql, data)
                connection.commit()

            connection.close()
        except Exception as ex:
            raise Exception(ex)
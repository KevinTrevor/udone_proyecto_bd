from database import get_connection
from .entities import Customer

class CustomerModel:

    @classmethod
    def insert_customers(self, data):
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
    def select_all_customers(self):
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
    def select_customer_by_cedula(self, cedula):
        """Función que selecciona a un cliente específico registrado en la base de datos"""

        sql = "SELECT * FROM cliente WHERE cedula = (%s)"

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql, (cedula, ))
                row = cursor.fetchone()
                
                customer = Customer(row[0], row[1], row[2], row[3])
        
            connection.close()
            return customer.to_JSON()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_customer(self, data):
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
from psycopg2 import Error
from database import get_connection

def insert_costumers(data):
    """Función que crea un nuevo cliente en la base de datos."""
    
    connection = get_connection()
    
    sql = "INSERT INTO cliente (cedula, nombre, whatsapp, email) VALUES(%s, %s, %s, %s);"
    
    pass
            
def select_all_costumers():
    """Función que selecciona a todos los clientes registrados en la base de datos"""
    pass

def update_costumer():
    pass
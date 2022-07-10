import psycopg2
from psycopg2 import DatabaseError

def get_connection():
    """Función que conecta con la base de datos. En caso de error, devuelve una excepción.

    Returns:
        connection: Devuelve la conexión con la base de datos.
    """
    
    conn = None
    try:
        conn = psycopg2.connect(
            host= "localhost",
            user= "postgres",
            password= "0905*KdR",
            database= "chikkins"
        )
    except DatabaseError as e:
        return e
    return conn
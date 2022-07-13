import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    """Función que conecta con la base de datos. En caso de error, devuelve una excepción.

    Returns:
        connection: Devuelve la conexión con la base de datos.
    """
    try:
        return psycopg2.connect(
            host= config('PGHOST'),
            user= config('PGUSER'),
            password= config('PGPASSWORD'),
            database= config('PGDATABASE')
        )
    except DatabaseError as ex:
        raise ex 
from psycopg2 import Error
from .connect import get_connection

def read_file(path):
    """Función que lee un archivo en un pathing especifico y retorna lo leído de un archivo."""
    with open(path, "r") as sql_file:
        return sql_file.read()

def create_tables():
    """Función que crea las tablas de una base de datos a través de código DDL."""

    connection = get_connection()

    path = "src/database/sql/chikkins.sql"

    sql = read_file(path)
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
    connection.close()
import psycopg2
from psycopg2 import DatabaseError

def get_connection():
    
    try:
        return psycopg2.connect()
    except DatabaseError as e:
        return e
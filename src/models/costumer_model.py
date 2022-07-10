from psycopg2 import Error
from database import get_connection

def insert_costumers(data):
    """Función que crea un nuevo cliente en la base de datos."""
    
    conn = get_connection()
    
    sql = f"INSERT INTO cliente (cedula, nombre, whatsapp, email) VALUES(%s, %s, %s, %s);"
    
    try:
        curs = conn.cursor()
        curs.execute(sql, data)
        conn.commit()
        
        return curs.lastrowid
    except Error as e:
        print(f"Error at insert_costumers(): {e}")
        return False
    finally:
        if conn:
            curs.close()
            conn.close()
            
def select_all_costumers():
    pass

def update_costumer():
    pass
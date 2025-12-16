import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST'),
            database=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            port=os.getenv('POSTGRES_PORT')
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la BD: {e}")
        return None

def execute_query(query, params=None, fetch=True):
    """Función helper para ejecutar SQL y devolver diccionarios"""
    conn = get_db_connection()
    if conn is None:
        return None
    
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            if fetch:
                result = cur.fetchall()
                return result
            else:
                conn.commit()
                return cur.rowcount
    except Exception as e:
        print(f"Error SQL: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()
import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_peliculas'
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None

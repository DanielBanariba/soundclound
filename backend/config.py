# Conexión Oracle: 1521
# MySQL: 3306
# pip install cx_Oracle

# Para poder conectar la base de datos Oracle con Python, tenemos que crear un entorno virtual, como?
# Ejecutamos el siguiente comando:
#  python -m venv /path/to/new/virtual/environment
# Después tenemos que irnos a la carpeta venv, scripts y por último activarlo, y ya estaremos en el entorno virtual de Python
import cx_Oracle


def oracle_config():

    # Configuración de la conexión Oracle
    config = {
        'user': 'system',
        'password': 'root1234',
        'dsn': 'localhost:1521/xe',  # Cambia esto según tu configuración
        'encoding': 'UTF-8'
    }

#Tenemos que poner un try Exception, para evitar cualquier error que pueda ocurrir en la base de datos
    try:
        connection = cx_Oracle.connect(**config)
        print(f"Conectado a Oracle Database {connection.version}")
        return config  # Devolver el diccionario de configuración
    except cx_Oracle.Error as err:
        print("Error de conexión a Oracle:", err)
        return None

if __name__ == "__main__":
    oracle_config()
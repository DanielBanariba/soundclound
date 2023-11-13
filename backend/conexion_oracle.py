# Conexión Oracle: 1521
# MySQL: 3306
# pip install cx_Oracle

# Para poder conectar la base de datos Oracle con Python, tenemos que crear un entorno virtual, como?
# Ejecutamos el siguiente comando:
#  python -m venv /path/to/new/virtual/environment
# Después tenemos que irnos a la carpeta venv, scripts y por último activarlo, y ya estaremos en el entorno virtual de Python


import oracledb


def conectar_a_oracle():
    connection = oracledb.connect(
        user='system',
        password='root1234',
        dsn='localhost:1521/XEPDB1',
        encoding='UTF-8'
    )
    print(connection.version)
    return connection


def imprimir_datos_de_la_base_de_datos():
    connection = conectar_a_oracle()

    # Imprimimos lo que tenemos en la base de datos
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sucursal")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()


if __name__ == "__main__":
    # Conectamos a la base de datos
    connection = conectar_a_oracle()

    # Imprimimos la información de la conexión
    print("Conectado a Oracle Database", connection.version)

    # Imprimimos los datos de la base de datos
    imprimir_datos_de_la_base_de_datos()

    # Cerramos la conexión
    connection.close()
    print("Conexión Finalizada")

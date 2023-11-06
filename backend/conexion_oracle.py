#Conection oracle: 1521
#mysql: 3306
#pip install cx_Oracle
#para poder conectar la base de datos oracle con python, tenemos que crear un entorno virtual, como?
#Ejecutamos el siguiente comando: 
#  python -m venv /path/to/new/virtual/environment
#Despues tenemos que irnos a la carpeta venv, scripts y por ultimo activarlo, y ya estaremos en el entorno virtual de python

import cx_Oracle

try:
    connection = cx_Oracle.connect(
        user='system',
        password='root1234',
        dsn='localhost:1521/XEPDB1',
        encoding='UTF-8'
    )
    print(connection.version)

    #imprimimos lo que tenemos en la base de datos
    ##cursor.execute("SELECT * FROM sucursal")
    #rows = cursor.fetchall()
    #for row in rows:
    #    print(row)
except Exception as ex:
    print("Error en la connexion a la base de datos", ex)
else:
    print("Conectado a Oracle Database", conexion.version)
finally:
    connection.close()
    print("Conexcion Finalizada")
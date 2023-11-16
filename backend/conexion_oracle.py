# Conexión Oracle: 1521
# MySQL: 3306
# pip install oracledb

# Para poder conectar la base de datos Oracle con Python, tenemos que crear un entorno virtual, como?
# Ejecutamos el siguiente comando:
#  python -m venv /path/to/new/virtual/environment
# Después tenemos que irnos a la carpeta venv, scripts y por último activarlo, y ya estaremos en el entorno virtual de Python
import oracledb

def conectar_a_oracle():
#Tenemos que poner un try Exception, para evitar cualquier error que pueda ocurrir en la base de datos
    try:
        connection = oracledb.connect(
            user='system',
            password='root1234',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(connection.version)
    except oracledb.Error as err:
        print("Error de conexcion a Oracle", err)
    else:
        print("Conectado a Oracle Database", connection.version)


     # Verificar si la tabla ya existe en el esquema 'system'
    cursor = connection.cursor()
    table_exists = False
    try:
        cursor.execute("SELECT count(*) FROM all_tables WHERE owner = 'SYSTEM' AND table_name = 'USER_DANIEL'")
        result = cursor.fetchone()
        if result[0] > 0:
            table_exists = True
    except oracledb.Error as err:
        print("Error al verificar la existencia de la tabla", err)
    
    if table_exists:
        print("No se puede crear una tabla existente")
    else:
        # Creamos la tabla usuarios
        cur_01 = connection.cursor()
        crear_tabla = """
            CREATE TABLE usuarios2f4 (
                id INT NOT NULL,
                name VARCHAR2(255) NOT NULL,
                author VARCHAR2(255) NOT NULL,
                duration INT NOT NULL,
                audio_blob BLOB NOT NULL,
                PRIMARY KEY (id)
            )
        """
        cur_01.execute(crear_tabla)
        print("Tabla creada exitosamente")
    
    #finally:
    connection.close()
    #    print("Conexcion finalizada")

    # con este codigo nos va a servir para poder seleccionar las tablas, e imprimir lo que contiene
    # Imprimimos lo que tenemos en la base de datos
    #cursor = connection.cursor()
    #cursor.execute("SELECT * FROM sucursal")
    #rows = cursor.fetchall()
    #for row in rows:
    #    print(row)

#La funcion principal donde tenemos que llamarla para que se pueda conectar correctamente a la base da datos
if __name__ == "__main__":
    conectar_a_oracle()
    
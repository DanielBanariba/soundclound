# Conexión Oracle: 1521
# MySQL: 3306
# pip install cx_Oracle

# Para poder conectar la base de datos Oracle con Python, tenemos que crear un entorno virtual, como?
# Ejecutamos el siguiente comando:
#  python -m venv /path/to/new/virtual/environment
# Después tenemos que irnos a la carpeta venv, scripts y por último activarlo, y ya estaremos en el entorno virtual de Python
import cx_Oracle

def conectar_a_oracle():
#Tenemos que poner un try Exception, para evitar cualquier error que pueda ocurrir en la base de datos
    try:
        connection = cx_Oracle.connect(
            #Poner los datos de su configuracion de oracle 
            user='system',
            password='root1234',
            dsn='localhost:1521/xe',
            encoding='UTF-8'
        )
        print(connection.version)
    except cx_Oracle.Error as err:
        print("Error de conexcion a Oracle", err)
    else:
        print("Conectado a Oracle Database", connection.version)


     # Verificar si la tabla ya existe en el esquema 'system'
    cursor = connection.cursor()
    table_exists = False
    try:
        cursor.execute("SELECT count(*) FROM ALL_TABLES WHERE owner = 'system' AND table_name = 'Metallica'")
        result = cursor.fetchone()
        if result[0] > 0:
            table_exists = True
    except cx_Oracle.Error as err:
        print("Error al verificar la existencia de la tabla", err)
        connection.close()
        return
    
    if table_exists:
        print("No se puede crear una tabla existente")
    else:
        # Creamos la tabla <<nombre de su tabla>>
        try:
            crear_tabla = """
                CREATE TABLE PCDET (
                    id INT NOT NULL,
                    name VARCHAR2(255) NOT NULL,
                    author VARCHAR2(255) NOT NULL,
                    duration INT NOT NULL,
                    audio_blob BLOB NOT NULL,
                    PRIMARY KEY (id)
                )
            """
            cursor.execute(crear_tabla)
            print("Tabla creada exitosamente")
        except cx_Oracle.Error as err:
            print("Error al crear la tabla", err)
    
    connection.close()
    print("Conexcion finalizada")

    # con este codigo nos va a servir para poder seleccionar las tablas, e imprimir lo que contiene
    # Imprimimos lo que tenemos en la base de datos
    #cursor = connection.cursor()
    #cursor.execute("SELECT * FROM sucursal")
    #rows = cursor.fetchall()
    #for row in rows:
    #    print(row)

    #Consultar tablas en la base de datos
    #cur_01=connection.cursor()
    #cur_01.execute('select * from dual')
    #result = cur_01.fetchall()

    #print(result)

#La funcion principal tenemos que invocarla para que se pueda conectar correctamente a la base da datos
if __name__ == "__main__":
    conectar_a_oracle()
import cx_Oracle
from config import conectar_a_oracle

connection = conectar_a_oracle

def crear_y_validar_tablas():
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
    crear_y_validar_tablas()
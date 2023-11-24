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
                CREATE TABLE Metallica (
                    id NUMBER PRIMARY KEY,
                    song_name VARCHAR2(100),
                    album_name VARCHAR2(100),
                    release_year NUMBER
                )
            """
            cursor.execute(crear_tabla)
            print("Tabla creada exitosamente")
        except cx_Oracle.Error as err:
            print("Error al crear la tabla", err)

    # Insertamos datos en la tabla creada anteriormente 
    insert_data = """
        INSERT INTO Metallica (id, song_name, album_name, release_year)
        VALUES (:id, :song_name, :album_name, :release_year)
    """
    cursor.execute(insert_data, [1, 'Enter Sandman', 'Metallica', 1991])    
    
    # Consultamos los datos de la tabla
    query = "SELECT * FROM Metallica WHERE release_year > 1990"
    cursor.execute(query)
    for row in cursor:
        print(row)

    
    
    connection.close()
    print("Conexcion finalizada")

#La funcion principal tenemos que invocarla para que se pueda conectar correctamente a la base da datos
if __name__ == "__main__":
    crear_y_validar_tablas()
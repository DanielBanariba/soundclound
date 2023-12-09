#Lo que pude entender es un CRUD, pero usando python, entonces...
#Podemos hacer un nuevo archivo en la carpeta routers, donde exista un archivo de administrador.py y esta se va a 
#Encargar en hacer el CRUD de la base de datos

from db.client import conectar_a_oracle

# Creamos la tabla audio_table
def crear_tabla_audio():
    connection = conectar_a_oracle()

    # Creamos la tabla
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE audio_table (
            id INT NOT NULL,
            name VARCHAR2(255) NOT NULL,
            author VARCHAR2(255) NOT NULL,
            duration INT NOT NULL,
            audio_blob BLOB NOT NULL,
            PRIMARY KEY (id)
        )
    """)

    connection.commit()
    connection.close()


#---------------------------------------------------------------------------------------------------------------------------------------

# Insertamos una fila en la tabla audio_table
def insertar_fila_audio(id, name, author, duration, file_path):
    connection = conectar_a_oracle()

    # Insertamos la fila
    cursor = connection.cursor()
    with open(file_path, "rb") as audio_file:
        audio_blob = audio_file.read()
    cursor.execute("""
        INSERT INTO audio_table (id, name, author, duration, audio_blob)
        VALUES (1, 'Canción 1', 'Autor 1', 300, '/path/to/file.mp3')
    """,                                        #Ruta donde va a ir los audios
        {"id": id, "name": name, "author": author, "duration": duration, "audio_blob": audio_blob})
    connection.commit()
    connection.close()


#---------------------------------------------------------------------------------------------------------------------------------------

# Actualizamos una fila en la tabla audio_table
def actualizar_fila_audio(id, name, author, duration, file_path):
    connection = conectar_a_oracle()

    # Actualizamos la fila
    cursor = connection.cursor()
    with open(file_path, "rb") as audio_file:
        audio_blob = audio_file.read()
    cursor.execute("""
        UPDATE audio_table
        SET name = :name, author = :author, duration = :duration, audio_blob = :audio_blob
        WHERE id = :id
    """, {"id": id, "name": name, "author": author, "duration": duration, "audio_blob": audio_blob})

    connection.commit()
    connection.close()


#---------------------------------------------------------------------------------------------------------------------------------------

# Eliminamos una fila en la tabla audio_table
def eliminar_fila_audio(id: int):
    connection = conectar_a_oracle()

    try:
        # Eliminamos la fila
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM audio_table
            WHERE id = :id
        """, {"id": id})

        connection.commit()
    finally:
        connection.close()


#---------------------------------------------------------------------------------------------------------------------------------------

#La funcion principal
if __name__ == "__main__":
    #crear_tabla_audio()
    #insertar_fila_audio()
    #actualizar_fila_audio()
    #eliminar_fila_audio()
    print("Si no esta esto, no se ejecuta el codigo")
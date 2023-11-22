from config import conectar_a_oracle
import cx_Oracle
# Obtener la configuración de la base de datos
configuracion = conectar_a_oracle()

# Conectar a la base de datos
connection = cx_Oracle.connect(**configuracion)


def agregar_audio(id, name, author, duration, file_path):
    cursor = connection.cursor()
    with open(file_path, "rb") as audio_file:
        audio_blob = audio_file.read()
    cursor.execute("INSERT INTO audio_table (id, name, author, duration, audio_blob) VALUES (:id, :name, :author, :duration, :audio_blob)",
                   {"id": id, "name": name, "author": author, "duration": duration, "audio_blob": audio_blob})
    connection.commit()
    cursor.close()
    connection.close()


def actualizar_audio(id, name, author, duration, file_path):
    cursor = connection.cursor()
    with open(file_path, "rb") as audio_file:
        audio_blob = audio_file.read()
    cursor.execute("UPDATE audio_table SET name = :name, author = :author, duration = :duration, audio_blob = :audio_blob WHERE id = :id",
                   {"id": id, "name": name, "author": author, "duration": duration, "audio_blob": audio_blob})
    connection.commit()
    cursor.close()
    connection.close()


def eliminar_audio(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM audio_table WHERE id = :id", {"id": id})
    connection.commit()
    cursor.close()
    connection.close()

#Si quieres ejecutar alguna funcion en especifico, solo quieta el comentario
if __name__ == "__main__":
    #agregar_audio()
    #actualizar_audio()
    #eliminar_audio()
    pass#Comenta esto
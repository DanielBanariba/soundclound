from config import conectar_a_oracle

def insertar_fila_audio(id, name, author, duration, file_path):
    connection = conectar_a_oracle()
    cursor = connection.cursor()
    with open(file_path, "rb") as audio_file:
        audio_blob = audio_file.read()
    cursor.execute("INSERT INTO audio_table (id, name, author, duration, audio_blob) VALUES (:id, :name, :author, :duration, :audio_blob)",
                   {"id": id, "name": name, "author": author, "duration": duration, "audio_blob": audio_blob})
    connection.commit()
    cursor.close()
    connection.close()

def actualizar_fila_audio(id, name, author, duration, file_path):
    connection = conectar_a_oracle()
    cursor = connection.cursor()
    with open(file_path, "rb") as audio_file:
        audio_blob = audio_file.read()
    cursor.execute("UPDATE audio_table SET name = :name, author = :author, duration = :duration, audio_blob = :audio_blob WHERE id = :id",
                   {"id": id, "name": name, "author": author, "duration": duration, "audio_blob": audio_blob})
    connection.commit()
    cursor.close()
    connection.close()

def eliminar_fila_audio(id):
    connection = conectar_a_oracle()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM audio_table WHERE id = :id", {"id": id})
    connection.commit()
    cursor.close()
    connection.close()
import cx_Oracle
import os
from config import conectar_a_oracle

# Obtener la configuración de la base de datos
configuracion = conectar_a_oracle()

# Conectar a la base de datos
connection = cx_Oracle.connect(**configuracion)

def insertar_archivo_mp3(ruta_archivo_mp3):
    # Crear un cursor
    cursor = connection.cursor()
    print(f"Intentando insertar el archivo MP3 desde la ruta: {ruta_archivo_mp3}")

    try:
        # Leer el archivo MP3 como bytes
        with open(ruta_archivo_mp3, "rb") as file:
            mp3_data = file.read()

        print("Archivo MP3 leído exitosamente ", mp3_data)

        # Insertar el archivo MP3 en la tabla
        cursor.execute("INSERT INTO system.AUDIOS (id, archivo_mp3) VALUES (seq.nextval, :mp3_data)", {'mp3_data': mp3_data})

        # Confirma la transacción
        connection.commit()

        # Imprime el ID del nuevo registro
        nuevo_id = cursor.execute("SELECT seq.currval FROM DUAL").fetchone()[0]
        print(f"Subida exitosa. Nuevo ID: {nuevo_id}")

    except Exception as e:
        print(f"Error al insertar el archivo MP3: {str(e)}")
    finally:
        # Cerrar el cursor solo si está abierto
        if cursor:
            cursor.close()

# Crear una secuencia si no existe, identificardores unicos para cada cancion, esto puede ser para cualquier objeto
try:
    cursor = connection.cursor()
    cursor.execute("CREATE SEQUENCE seq START WITH 1 INCREMENT BY 1")
    print("Secuencia creada exitosamente")
    cursor.close()
except cx_Oracle.DatabaseError as e:
    if "ORA-00955" in str(e):
        print("La secuencia ya existe")
    else:
        raise

# Obtener la lista de archivos en el directorio
archivos_mp3 = os.listdir("C:\\Users\\banar\\Desktop\\soundclound\\backend\\audios")

# Iterar sobre la lista de archivos e insertar cada uno
for archivo_mp3 in archivos_mp3:
    ruta_completa = os.path.join("C:\\Users\\banar\\Desktop\\soundclound\\backend\\audios", archivo_mp3)
    insertar_archivo_mp3(ruta_completa)
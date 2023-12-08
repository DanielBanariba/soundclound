# Tengo una tabla que se llama TBL_CANCIONES y tiene los siguientes campos P*ID_CANCION, TITULO, NUMERO DE CANCION, ANIO, ID_GENERO, DURACION, y tengo otra tabla que se llama TBL_AUDIOS y tiene como campos PF*ID_CANCION, ID_COPYRIGHT, ARCHIVO_MP3 y PORTADA, en archivo_mp3 y portada solo guardan el directorio de los archivos, ahora bien, quiero que agarres el titulo de TBL_CANCIONES y lo compares con el titulo del archivo que esta en la carpeta audios si los dos titulos coinciden como por ejemplo Sucesor==Sucesor entonces le vas a poner el ID_CANCION al la tabla TBL_AUDIOS 

import cx_Oracle, os, eyed3, sys
sys.path.append(os.path.join(os.getcwd(), 'backend'))#Obtener la ruta del directorio actual y concatenarla con el subdirectorio de los archivos de audio
from config import conectar_a_oracle

# Obtener la ruta del directorio actual
directorio_actual = os.getcwd()

# Concatenar la ruta del directorio actual con el subdirectorio de los archivos de audio
ruta_audios = os.path.join(directorio_actual, 'backend', 'audios')

# Obtener la configuración de la base de datos
configuracion = conectar_a_oracle()

# Conectar a la base de datos
connection = cx_Oracle.connect(**configuracion)

def insertar_archivo_mp3(ruta_archivo_mp3):
    # Crear un cursor
    cursor = connection.cursor()
    print(f"Intentando insertar el archivo MP3 desde la ruta: {ruta_archivo_mp3}")

    # Obtener el título del archivo MP3
    titulo_archivo_mp3 = os.path.splitext(os.path.basename(ruta_archivo_mp3))[0]

    try:
        # Buscar en la tabla TBL_CANCIONES para obtener el ID_CANCION correspondiente al título del archivo MP3
        cursor.execute("SELECT ID_CANCION FROM TBL_CANCIONES WHERE TITULO = :titulo", titulo=titulo_archivo_mp3)
        id_cancion = cursor.fetchone()[0]

        # Insertar el ID_CANCION en la tabla TBL_AUDIOS
        cursor.execute("UPDATE TBL_AUDIOS SET ID_CANCION = :id_cancion WHERE TITULO = :titulo", id_cancion=id_cancion, titulo=titulo_archivo_mp3)

        # Confirmar la transacción
        connection.commit()

        print(f"Archivo MP3 insertado con éxito: {ruta_archivo_mp3}")

    except Exception as e:
        print(f"Error al insertar el archivo MP3: {ruta_archivo_mp3}")
        print(e)

    finally:
        # Cerrar el cursor
        cursor.close()
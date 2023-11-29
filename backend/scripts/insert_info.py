import os, eyed3, cx_Oracle
from config import conectar_a_oracle

# Obtener la ruta del directorio actual
directorio_actual = os.getcwd()

# Concatenar la ruta del directorio actual con el subdirectorio de los archivos de audio
ruta_audios = os.path.join(directorio_actual, 'backend', 'audios')


# Conectar a la base de datos
configuracion = conectar_a_oracle()
connection = cx_Oracle.connect(**configuracion)
cursor = connection.cursor()

def extraer_info_mp3(ruta_archivo_mp3):
    # Cargar el archivo MP3
    audiofile = eyed3.load(ruta_archivo_mp3)

    # Extraer la información
    titulo = audiofile.tag.title
    artista = audiofile.tag.artist
    album = audiofile.tag.album
    anio = audiofile.tag.getBestDate()
    numero_cancion = audiofile.tag.track_num[0]
    genero = audiofile.tag.genre.name
    duracion = audiofile.info.time_secs

    return titulo, artista, album, anio, numero_cancion, genero, duracion

def insertar_info_db(info):
    titulo, artista, album, anio, numero_cancion, genero, duracion = info

    # Insertar la información en la base de datos
    cursor.execute("INSERT INTO TB_ALBUM (Nombre, anio) VALUES (:1, :2)", (album, anio))
    cursor.execute("INSERT INTO TB_ARTISTAS (Nombre) VALUES (:1)", (artista,))
    cursor.execute("INSERT INTO TB_GENERO (Nombre) VALUES (:1)", (genero,))
    connection.commit()

# Obtener la lista de archivos en el directorio
archivos_mp3 = os.listdir(ruta_audios)

# Iterar sobre la lista de archivos e insertar la información de cada uno
for archivo_mp3 in archivos_mp3:
    ruta_completa = os.path.join(ruta_audios, archivo_mp3)
    info = extraer_info_mp3(ruta_completa)
    insertar_info_db(info)

# Cerrar la conexión a la base de datos
cursor.close()
connection.close()
import cx_Oracle, os, eyed3, sys
sys.path.append(os.path.join(os.getcwd(), 'backend'))
from config import conectar_a_oracle
from datetime import datetime, timedelta
from cx_Oracle import Date

# Obtener la ruta del directorio actual
directorio_actual = os.getcwd()

# Concatenar la ruta del directorio actual con el subdirectorio de los archivos de audio
ruta_audios = os.path.join(directorio_actual, 'backend', 'audios')

# Conectar a la base de datos
configuracion = conectar_a_oracle()
connection = cx_Oracle.connect(**configuracion)
cursor = connection.cursor()

# Leer todos los archivos de audio en la carpeta 'audios'
for filename in os.listdir(ruta_audios):
    if filename.endswith(".mp3"):
        # Extraer la información del archivo de audio
        audiofile = eyed3.load(os.path.join(ruta_audios, filename))
        print(f"Ruta del archivo: {os.path.join(ruta_audios, filename)}")
        print(f"Título de la canción: {audiofile.tag.title}") 
        print(f"Género del audio: {audiofile.tag.genre.name}")

        titulo = audiofile.tag.title
        numero_cancion = audiofile.tag.track_num[0]
        anio = audiofile.tag.getBestDate().year
        anio_date = datetime(year=anio, month=1, day=1)
        genero = audiofile.tag.genre.name
        duracion = timedelta(seconds=int(audiofile.info.time_secs))
            # Comparar el género de la canción con los géneros en la base de datos
        cursor.execute("SELECT ID_GENERO FROM TBL_GENERO WHERE Nombre = :1", (genero,))
        result = cursor.fetchone()
        
        if result is not None:
            # Si hay una coincidencia, guardar la información de la canción en la base de datos con el ID de género correspondiente
            cursor.execute("INSERT INTO TBL_CANCIONES (titulo, numero_cancion, anio, duracion, id_genero) VALUES (:1, :2, :3, :4, :5)",
                           (titulo, numero_cancion, anio_date, duracion, result[0]))
        # # Obtener el ID_GENERO de la tabla TBL_GENERO
        # id_genero = cursor.execute(f"SELECT ID_GENERO FROM TBL_GENERO WHERE LOWER(NOMBRE) = '{genero.lower()}'").fetchone()[0]

        # # Insertar los datos en la tabla TBL_CANCIONES
        # cursor.execute(f"INSERT INTO TBL_CANCIONES (TITULO, NUMERO_CANCION, ANIO, ID_GENERO, DURACION) VALUES ('{titulo}', {numero_cancion}, {anio}, {id_genero}, '{duracion}')")
        # # # Comparar el género del audio con los géneros en la base de datos
        # if cursor.execute(f"SELECT * FROM TBL_GENERO WHERE LOWER(NOMBRE) = '{genero.lower()}'").fetchone():
        #     id_genero = cursor.execute(f"SELECT ID_GENERO FROM TBL_GENERO WHERE LOWER(NOMBRE) = '{genero.lower()}'").fetchone()[0]
        #     print(f"ID de género obtenido de la base de datos: {id_genero}")

# Confirmar los cambios y cerrar la conexión a la base de datos
connection.commit()
cursor.close()
connection.close()
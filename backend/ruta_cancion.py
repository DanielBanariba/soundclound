# Donde se va a subir la ruta exacta de la cancion y se va a insertar en la base de datos para despues poder reproducirlo

import cx_Oracle, os
from config import conectar_a_oracle

# Obtener la configuración de la base de datos
configuracion = conectar_a_oracle()

# Conectar a la base de datos
connection = cx_Oracle.connect(**configuracion)

def insertar_ruta(ruta_archivo_mp3):
    # Crear un cursor
    cursor = connection.cursor()

    # Ejecutar la sentencia SQL INSERT
    cursor.execute("INSERT INTO AUDIOS (id, archivo_mp3) VALUES (seq.nextval, :ruta)", ruta=ruta_archivo_mp3)

    # Confirmar la transacción
    connection.commit()

    # Cerrar el cursor
    cursor.close()

    # Extraer el nombre de la canción de la ruta del archivo
    nombre_cancion = os.path.basename(ruta_archivo_mp3)

    # Imprimir el mensaje
    print(f"La canción '{nombre_cancion}' ha sido insertada exitosamente")
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

# Directorio que contiene los archivos de música
directorio_musica = r"C:\Users\banar\Desktop\soundclound\backend\audios"

# Recorrer el directorio de música
for raiz, dirs, archivos in os.walk(directorio_musica):
    for archivo in archivos:
        # Si el archivo es un archivo de música, insertar su ruta en la base de datos
        if archivo.endswith('.mp3'):
            ruta_archivo = os.path.join(raiz, archivo)
            insertar_ruta(ruta_archivo)
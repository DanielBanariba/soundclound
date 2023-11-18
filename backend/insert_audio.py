import cx_Oracle
from config import oracle_config

# Obtener la configuración de la base de datos
configuracion = oracle_config()

# Conectar a la base de datos
connection = cx_Oracle.connect(**configuracion)

def insertar_archivo_mp3(ruta_archivo_mp3):
    # Crear un cursor
    cursor = connection.cursor()

    try:
        # Leer el archivo MP3 como bytes
        with open(ruta_archivo_mp3, "rb") as file:
            mp3_data = file.read()

        # Insertar el archivo MP3 en la tabla
        cursor.execute("INSERT INTO tu_esquema.audios (id, archivo_mp3) VALUES (seq.nextval, :mp3_data)", {'mp3_data': mp3_data})

        # Confirmar la transacción
        connection.commit()

        print("Inserción exitosa")
    except Exception as e:
        print(f"Error al insertar el archivo MP3: {str(e)}")
    finally:
        # Cerrar el cursor
        cursor.close()

# Uso de la función para insertar un archivo MP3
insertar_archivo_mp3("C:\\Users\\banar\\Desktop\\soundclound\\backend\\audios\\Satan.mp3")
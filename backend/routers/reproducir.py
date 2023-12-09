from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
#exporta la configuracion ya creada de la base de datos
from db.client import conectar_a_oracle
import cx_Oracle, io
from fastapi.templating import Jinja2Templates
from fastapi import Depends
from starlette.responses import Response

templates = Jinja2Templates(directory="./static/templates")

configuracion = conectar_a_oracle()# Obtener la configuración de la base de datos
connection = cx_Oracle.connect(**configuracion)# Conectar a la base de datos

cursor = connection.cursor()

# Configuracion para la url y el mensaje personalizado
router = APIRouter(prefix="/reproducir",  
                    tags=["reproducir"], 
                    responses={404: {"message": "Cancion no encontrado"}})

# Ruta para obtener y reproducir el archivo de audio
@router.get("/canciones")
async def get_all_audios():
    # Consulta para obtener todos los audios desde la base de datos
    query = "SELECT * FROM AUDIOS"
    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        # Crear una lista para almacenar los resultados
        audios = []
        # Iterar sobre los resultados y agregar cada uno a la lista
        for result in results:
            audio = {
                'id': result[0],
                'ruta_archivo': result[1],
                # Agregar más campos aquí si es necesario
            }
            audios.append(audio)

        # Devolver la lista como una respuesta JSON
        return audios
    else:
        raise HTTPException(status_code=404, detail="No se encontraron audios")

# Ruta para obtener y reproducir el archivo de audio
@router.get("/{audio_id}")
async def get_audio(audio_id: int):
    # Consulta para obtener el archivo binario desde la base de datos
    query = "SELECT archivo_mp3 FROM AUDIOS WHERE ID = :audio_id"
    cursor.execute(query, {'audio_id': audio_id})
    result = cursor.fetchone()

    if result:
        # Leer el archivo de música desde la ruta
        ruta_archivo = result[0]
        with open(ruta_archivo, 'rb') as f:
            audio_data = f.read()

        # Crear una respuesta de transmisión para el archivo de música
        try:
            return StreamingResponse(io.BytesIO(audio_data), media_type="audio/mp3")
        # Mensaje de error personalizado cuando el cliente cierra la conexión antes de que se complete la transmisión del archivo de audio 
        except ConnectionResetError:
            return Response("La conexión fue cerrada por el cliente", status_code=400)
    else:
        raise HTTPException(status_code=404, detail="Audio no encontrado")
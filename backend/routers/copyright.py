#Una nueva idea es subir el archivo codificado en binario en una nuena tabla que tenga el mismo nombre, pero sacando el audio de la tabla a udio, convirtiendolo en binario y al tenerlo en binario subirlo a la tabla copyright

# Se muestran las canciones con derechos de autor, si la cancion se reproduce, es porque ya esta registrado en la base de datos y no se puede volver a subir
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
#exporta la configuracion ya creada de la base de datos
from config import conectar_a_oracle
import cx_Oracle, io
from fastapi.templating import Jinja2Templates
from fastapi import Depends
from starlette.responses import Response

templates = Jinja2Templates(directory="./static/templates")

configuracion = conectar_a_oracle()# Obtener la configuración de la base de datos
connection = cx_Oracle.connect(**configuracion)# Conectar a la base de datos

cursor = connection.cursor()

# Configuracion para la url y el mensaje personalizado
router = APIRouter(prefix="/copyright",  
                    tags=["copyright"], 
                    responses={404: {"message": "Cancion no encontrado"}})


# Ruta para obtener las canciones con derechos de autor
@router.get("/{audio_id}")
async def get_audio(audio_id: int):
    # Consulta para obtener el archivo binario desde la base de datos
    query = "SELECT ARCHIVO_MP3 FROM AUDIOS WHERE ID = :audio_id"
    cursor.execute(query, {'audio_id': audio_id})
    result = cursor.fetchone()

    if result:
        # Decodifica el archivo binario
        audio_data = result[0].read()
        # Crear una respuesta de transmisión para el archivo
        try:
            return StreamingResponse(io.BytesIO(audio_data), media_type="audio/mp3")
        #Mensaje de error personalizado cuando el cliente cierra la conexión antes de que se complete la transmisión del archivo de audio 
        except ConnectionResetError:
            return Response("La conexión fue cerrada por el cliente", status_code=400)
    else:
        raise HTTPException(status_code=404, detail="Audio no encontrado")

#COMENTARIO-OJO CON ESTO!
#Funciona bien cuando llamamos a la cancion, pero en la consola por alguna extranna razon que desconozco, me tira el 
#200ok pero al mismo tiempo tira el 404 Not Found, tenemos que revisar porque pasa eso
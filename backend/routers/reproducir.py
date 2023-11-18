from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
#exporta la configuracion ya creada de la base de datos
from config import conectar_a_oracle
import cx_Oracle, io


configuracion = conectar_a_oracle()# Obtener la configuración de la base de datos
connection = cx_Oracle.connect(**configuracion)# Conectar a la base de datos

# Conexión a la base de datos Oracle
                                    #puerto de oracle y el nombre del servicio de nuestra base de datos
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe')#OJO! hecharle una revisada ya que tiene la mismos datos que en el config.py
cursor = connection.cursor()

# Configuracion para la url y el mensaje personalizado
router = APIRouter(prefix="/reproducir",  
                    tags=["reproducir"], 
                    responses={404: {"message": "Cancion no encontrado"}})


# Ruta para obtener y reproducir el archivo de audio
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
        return StreamingResponse(io.BytesIO(audio_data), media_type="audio/mp3")
    else:
        raise HTTPException(status_code=404, detail="Audio no encontrado")
    
#COMENTARIO-OJO CON ESTO!
#Funciona bien cuando llamamos a la cancion, pero en la consola por alguna extranna razon que desconozco, me tira el 
#200ok pero al mismo tiempo tira el 404 Not Found, tenemos que revisar porque pasa eso
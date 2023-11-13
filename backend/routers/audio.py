import conexion_oracle

from fastapi import APIRouter
from fastapi.responses import FileResponse, StreamingResponse #Investigar mas sobre el StreamingResponse

router = APIRouter(prefix="/audio", 
                    tags=["audio"], 
                    responses={404: {"message": "Cancion no encontrado"}})


@router.get("/{id}")
async def get_audio(id: int):
    # Recupera la cancion de la base de datos
    cursor = conexion_oracle.connection.cursor()
    cursor.execute("SELECT audio_blob FROM audio_table WHERE id = :id", {"id": id})
    audio_blob = cursor.fetchone()[0].read() 

    # Cierra el cursor de la base de datos
    cursor.close()

    # Devuelve la cancion(Archivo de audio) como respuesta
    return FileResponse(audio_blob, media_type="audio/mpeg")
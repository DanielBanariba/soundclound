from fastapi import APIRouter
from fastapi.responses import FileResponse, StreamingResponse
from conexion_oracle import conectar_a_oracle

router = APIRouter(prefix="/audio",
                    tags=["audio"],
                    responses={404: {"message": "Canción no encontrada"}})


@router.get("/{id}")
async def get_audio(id: int):

    # Conectamos a la base de datos
    connection = conectar_a_oracle()

    # Recuperamos la canción de la base de datos
    cursor = connection.cursor()
    cursor.execute("SELECT audio_blob FROM audio_table WHERE id = :id", {"id": id})
    audio_blob = cursor.fetchone()[0].read()

    # Cerramos el cursor de la base de datos
    cursor.close()

    # Devolvemos la canción (Archivo de audio) como respuesta
    return FileResponse(audio_blob, media_type="audio/mpeg")
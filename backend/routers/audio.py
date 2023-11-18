from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from config import oracle_config

router = APIRouter(prefix="/audio",
                    tags=["audio"],
                    responses={404: {"message": "Canción no encontrada"}})


@router.post("/")
async def crear_audio(id: int, name: str, author: str, duration: int, audio_file: UploadFile = File(...)):
    file_path = f"audios/{audio_file.filename}"
    with open(file_path, "wb") as audio:
        content = await audio_file.read()
        audio.write(content)
    insertar_fila_audio(id, name, author, duration, file_path)
    return {"message": "Canción creada exitosamente"}

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
    return StreamingResponse(audio_blob, media_type="audio/mpeg")#tenemoos que probar remplazar el StreamingResponse, por el FileResponse

@router.put("/{id}")
async def actualizar_audio(id: int, name: str, author: str, duration: int, audio_file: UploadFile = File(...)):
    file_path = f"audios/{audio_file.filename}"
    with open(file_path, "wb") as audio:
        content = await audio_file.read()
        audio.write(content)
    actualizar_fila_audio(id, name, author, duration, file_path)
    return {"message": "Canción actualizada exitosamente"}

@router.delete("/{id}")
async def eliminar_audio(id: int):
    eliminar_fila_audio(id)
    return {"message": "Canción eliminada exitosamente"}
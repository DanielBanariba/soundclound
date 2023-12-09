from pydantic import BaseModel

class Canciones(BaseModel):
    id_cancion: int
    id_copyriht: int
    archivo_mp3: str
    portada: str
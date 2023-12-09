from pydantic import BaseModel

class Playlist(BaseModel):
    id_playlist: int
    id_oyente: int
    nombre: str
    fecha_creacion: int
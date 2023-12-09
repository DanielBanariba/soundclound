from pydantic import BaseModel

class Artistas(BaseModel):
    id_artista: int
    id_oyente: int
    nombre_artista: str
    descripcion: str
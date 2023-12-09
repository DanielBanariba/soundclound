from pydantic import BaseModel

class LetrasCanciones(BaseModel):
    id_letra_cancion: int
    id_idioma: int
    id_cancion: int
    descripcion: str
    archivo: str
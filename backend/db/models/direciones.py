from pydantic import BaseModel

class Direccion(BaseModel):
    id_direccion: int
    id_ciudad: int
    descripcion: str
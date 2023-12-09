from pydantic import BaseModel

class Genero(BaseModel):
    id_genero: int
    nombre: str
    descripcion_genero: str
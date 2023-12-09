from pydantic import BaseModel

class Oyentes(BaseModel):
    id_oyentes: int
    id_usuario: int
    descripcion_oyente: str
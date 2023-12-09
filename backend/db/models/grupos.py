from pydantic import BaseModel

class Grupos(BaseModel):
    id_grupo: int
    id_oyente: int
    nombre_banda: str
    descripcion: str
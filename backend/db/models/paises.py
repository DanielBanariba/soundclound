from pydantic import BaseModel

class Paises(BaseModel):
    id_pais: int
    nombre_pais: str
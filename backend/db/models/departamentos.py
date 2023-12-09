from pydantic import BaseModel

class Departamentos(BaseModel):
    id_departamento: int
    id_pais: int
    nombre_departamento: str
from pydantic import BaseModel

class Ciudades(BaseModel):
    id_ciudad: int
    id_departamento: int
    nombre_ciudad: str
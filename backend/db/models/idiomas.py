from pydantic import BaseModel

class Idiomas(BaseModel):
    id_idioma: int
    nombre_idioma: str
    abreviatura: str
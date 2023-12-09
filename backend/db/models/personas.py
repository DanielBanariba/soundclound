import datetime
from pydantic import BaseModel

class Personas(BaseModel):
    id_persona: int
    numero_id: int
    nombre: str
    apellido: str
    fecha_de_nacimiento: datetime.date
    correo: str
    telefono: int
    genero: str
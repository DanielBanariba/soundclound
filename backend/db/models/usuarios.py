import datetime
from pydantic import BaseModel

class Usuario(BaseModel):
    id_usuario: int
    id_tipo_usuario: int
    id_membresia: int
    id_direccion: int
    nombre_usuario: str
    fecha_registro: datetime.date
    clave: str
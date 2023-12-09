from datetime import date
from pydantic import BaseModel

class Membresia(BaseModel):
    id_membresia: int
    id_tipo_membresia: int
    fecha_inicio: date.datetime
    fecha_vencimiento: date.datetime
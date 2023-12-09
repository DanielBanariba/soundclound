import datetime
from pydantic import BaseModel

class Canciones(BaseModel):
    id_cancion: int
    titulo: str
    numero_cancion: int
    anio: datetime.date
    id_genero: int
    duracion: int
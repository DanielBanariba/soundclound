import datetime
from pydantic import BaseModel

class Album(BaseModel):
    id_album: int
    id_artista: int
    id_grupo: int
    nombre: str
    anio: datetime.date
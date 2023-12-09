from datetime import date
from pydantic import BaseModel

class Shares(BaseModel):
    id_share: int
    id_plataforma: int
    id_oyente: int
    id_playlist: int
    id_cancion: int
    fecha_share: date.datetime
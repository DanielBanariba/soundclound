from datetime import date
from pydantic import BaseModel

class Escuchas(BaseModel):
    id_escucha: int
    id_oyente: int
    id_cancion: int
    fecha_escucha: date.datetime
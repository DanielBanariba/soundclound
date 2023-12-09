from datetime import date
from pydantic import BaseModel

class Likes(BaseModel):
    id_like: int
    id_oyent: int
    id_cancion: int
    fecha_like: date.datetime
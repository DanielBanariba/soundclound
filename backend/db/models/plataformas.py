import datetime
from pydantic import BaseModel

class Plataformas(BaseModel):
    id_plataforma: int
    nombre_plataforma: str
    url_plataforma: str
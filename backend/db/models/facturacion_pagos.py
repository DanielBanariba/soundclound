import datetime
from pydantic import BaseModel

class FacturacionPagos(BaseModel):
    id_facturacion: int
    id_tipo_membresia: int
    fecha_inicio: datetime.datetime
    fecha_fin: datetime.datetime
    monto: int
    descuento_facturacion: int
from typing import List
from fastapi import APIRouter, HTTPException, status
from db.client import conectar_a_oracle
import cx_Oracle
from db.models.facturacion_pagos import FacturacionPagos

configuracion = conectar_a_oracle()
connection = cx_Oracle.connect(**configuracion)
cursor = connection.cursor()

router = APIRouter(prefix="/facturacion_pagos",  
                    tags=["facturacion_pagos"], 
                    responses={404: {"message": "ID no encontrado"}})

@router.get("/", response_model=List[FacturacionPagos])
async def get_items():
    cursor.execute("SELECT * FROM TBL_FACTURACION_PAGOS") 
    rows = cursor.fetchall()
    return [FacturacionPagos(id_facturacion=row[0], id_tipo_membresia=row[1], fecha_inicio=row[2], fecha_fin=row[3], monto=row[4], descuento_facturacion=row[5]) for row in rows]

@router.get("/{id_facturacion}", response_model=FacturacionPagos)
async def get_item(id_facturacion: int):
    cursor.execute("SELECT * FROM TBL_FACTURACION_PAGOS WHERE ID_FACTURACION = :id", {"id": id_facturacion})
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Facturacion no encontrado")
    return FacturacionPagos(id_facturacion=row[0], id_tipo_membresia=row[1], fecha_inicio=row[2], fecha_fin=row[3], monto=row[4], descuento_facturacion=row[5])

@router.post("/", response_model=FacturacionPagos, status_code=201)
async def create_item(item: FacturacionPagos):
    cursor.execute("INSERT INTO TBL_FACTURACION_PAGOS (ID_TIPO_MEMBRESIA, FECHA_INICIO, FECHA_FIN, MONTO, DESCUENTO_FACTURACION) VALUES (:id_tipo_membresia, :fecha_inicio, :fecha_fin, :monto, :descuento_facturacion)", {"id_tipo_membresia": item.id_tipo_membresia, "fecha_inicio": item.fecha_inicio, "fecha_fin": item.fecha_fin, "monto": item.monto, "descuento_facturacion": item.descuento_facturacion})
    connection.commit()
    return item

@router.put("/{id_facturacion}", response_model=FacturacionPagos)
async def update_item(id_facturacion: int, item: FacturacionPagos):
    cursor.execute("UPDATE TBL_FACTURACION_PAGOS SET ID_TIPO_MEMBRESIA = :id_tipo_membresia, FECHA_INICIO = :fecha_inicio, FECHA_FIN = :fecha_fin, MONTO = :monto, DESCUENTO_FACTURACION = :descuento_facturacion WHERE ID_FACTURACION = :id", {"id_tipo_membresia": item.id_tipo_membresia, "fecha_inicio": item.fecha_inicio, "fecha_fin": item.fecha_fin, "monto": item.monto, "descuento_facturacion": item.descuento_facturacion, "id": id_facturacion})
    connection.commit()
    cursor.execute("SELECT * FROM TBL_FACTURACION_PAGOS WHERE ID_FACTURACION = :id", {"id": id_facturacion})
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Facturacion no encontrado")
    return FacturacionPagos(id_facturacion=row[0], id_tipo_membresia=row[1], fecha_inicio=row[2], fecha_fin=row[3], monto=row[4], descuento_facturacion=row[5])

@router.delete("/{id_facturacion}")
async def delete_item(id_facturacion: int):
    cursor.execute("DELETE FROM TBL_FACTURACION_PAGOS WHERE ID_FACTURACION = :id", {"id": id_facturacion})
    connection.commit()
    return {"message": "Facturacion eliminado correctamente"}


from typing import List
from fastapi import APIRouter, HTTPException, status
from db.client import conectar_a_oracle
import cx_Oracle
from db.models.canciones import Canciones

configuracion = conectar_a_oracle()
connection = cx_Oracle.connect(**configuracion)
cursor = connection.cursor()

router = APIRouter(prefix="/canciones",  
                    tags=["canciones"], 
                    responses={404: {"message": "ID no encontrado"}})

@router.get("/", response_model=List[Canciones])
async def get_items():
    cursor.execute("SELECT * FROM TBL_CANCIONES") 
    rows = cursor.fetchall()
    return [Canciones(id_cancion=row[0], titulo=row[1], numero_cancion=row[2], anio=row[3], id_genero=row[4], duracion=row[5]) for row in rows]

@router.get("/{id_cancion}", response_model=Canciones)
async def get_item(id_cancion: int):
    cursor.execute("SELECT * FROM TBL_CANCIONES WHERE ID_CANCION = :id", {"id": id_cancion})
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Cancion no encontrada")
    return Canciones(id_cancion=row[0], titulo=row[1], numero_cancion=row[2], anio=row[3], id_genero=row[4], duracion=row[5])

@router.post("/", response_model=Canciones, status_code=201)
async def create_item(item: Canciones):
    cursor.execute("INSERT INTO TBL_CANCIONES (TITULO, NUMERO_CANCION, ANIO, ID_GENERO, DURACION) VALUES (:titulo, :numero_cancion, :anio, :id_genero, :duracion)", {"titulo": item.titulo, "numero_cancion": item.numero_cancion, "anio": item.anio, "id_genero": item.id_genero, "duracion": item.duracion})
    connection.commit()
    return item

@router.put("/{id_cancion}", response_model=Canciones)
async def update_item(id_cancion: int, item: Canciones):
    cursor.execute("UPDATE TBL_CANCIONES SET TITULO = :titulo, NUMERO_CANCION = :numero_cancion, ANIO = :anio, ID_GENERO = :id_genero, DURACION = :duracion WHERE ID_CANCION = :id", {"titulo": item.titulo, "numero_cancion": item.numero_cancion, "anio": item.anio, "id_genero": item.id_genero, "duracion": item.duracion, "id": id_cancion})
    connection.commit()
    cursor.execute("SELECT * FROM TBL_CANCIONES WHERE ID_CANCION = :id", {"id": id_cancion})
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Cancion no encontrada")
    return Canciones(id_cancion=row[0], titulo=row[1], numero_cancion=row[2], anio=row[3], id_genero=row[4], duracion=row[5])

@router.delete("/{id_cancion}")
async def delete_item(id_cancion: int):
    cursor.execute("DELETE FROM TBL_CANCIONES WHERE ID_CANCION = :id", {"id": id_cancion})
    connection.commit()
    return {"message": "Cancion eliminada correctamente"}



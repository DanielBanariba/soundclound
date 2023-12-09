from typing import List
from fastapi import APIRouter, HTTPException, status
from db.client import conectar_a_oracle
import cx_Oracle
from db.models.artistas import Artistas

configuracion = conectar_a_oracle()
connection = cx_Oracle.connect(**configuracion)
cursor = connection.cursor()

router = APIRouter(prefix="/artistas",  
                    tags=["artistas"], 
                    responses={404: {"message": "ID no encontrado"}})

@router.get("/", response_model=List[Artistas])
async def get_items():
    cursor.execute("SELECT * FROM TBL_ARTISTAS") 
    rows = cursor.fetchall()
    return [Artistas(id_artista=row[0], id_oyente=row[1], nombre_artista=row[2], descripcion=row[3]) for row in rows]

@router.get("/{id_artista}", response_model=Artistas)
async def get_item(id_artista: int):
    cursor.execute("SELECT * FROM TBL_ARTISTAS WHERE ID_ARTISTA = :id", {"id": id_artista})
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Artista no encontrado")
    return Artistas(id_artista=row[0], id_oyente=row[1], nombre_artista=row[2], descripcion=row[3])

@router.post("/", response_model=Artistas, status_code=201)
async def create_item(item: Artistas):
    cursor.execute("INSERT INTO TBL_ARTISTAS (ID_OYENTE, NOMBRE_ARTISTA, DESCRIPCION) VALUES (:id_oyente, :nombre_artista, :descripcion)", {"id_oyente": item.id_oyente, "nombre_artista": item.nombre_artista, "descripcion": item.descripcion})
    connection.commit()
    return item

@router.put("/{id_artista}", response_model=Artistas)
async def update_item(id_artista: int, item: Artistas):
    cursor.execute("UPDATE TBL_ARTISTAS SET ID_OYENTE = :id_oyente, NOMBRE_ARTISTA = :nombre_artista, DESCRIPCION = :descripcion WHERE ID_ARTISTA = :id", {"id_oyente": item.id_oyente, "nombre_artista": item.nombre_artista, "descripcion": item.descripcion, "id": id_artista})
    connection.commit()
    cursor.execute("SELECT * FROM TBL_ARTISTAS WHERE ID_ARTISTA = :id", {"id": id_artista})
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Artista no encontrado")
    return Artistas(id_artista=row[0], id_oyente=row[1], nombre_artista=row[2], descripcion=row[3])

@router.delete("/{id_artista}")
async def delete_item(id_artista: int):
    cursor.execute("DELETE FROM TBL_ARTISTAS WHERE ID_ARTISTA = :id", {"id": id_artista})
    connection.commit()
    return {"message": "Artista eliminado correctamente"}

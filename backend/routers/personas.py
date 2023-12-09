from typing import List
from fastapi import APIRouter, HTTPException, status
from db.client import conectar_a_oracle
import cx_Oracle
from db.models.personas import Personas

configuracion = conectar_a_oracle()
connection = cx_Oracle.connect(**configuracion)
cursor = connection.cursor()

router = APIRouter(prefix="/personas",  
                    tags=["personas"], 
                    responses={404: {"message": "ID no encontrado"}})

@router.get("/", response_model=List[Personas])
async def get_items():
    cursor.execute("SELECT * FROM TBL_PERSONAS") 
    rows = cursor.fetchall()
    return [Personas(id_persona=row[0], numero_id=[1], nombre=row[2], apellido=row[3], fecha_de_nacimiento=[4], correo=row[5], telefono=row[6], genero=row[7]) for row in rows]

@router.get("/{id_persona}", response_model=Personas)
async def get_item(id_persona: int):
    cursor.execute("SELECT * FROM TBL_PERSONAS WHERE ID_PERSONA = :id", {"id": id_persona})
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Persona no encontrado")
    return Personas(id_persona=row[0], numero_id=[1], nombre=row[2], apellido=row[3], fecha_de_nacimiento=[4], correo=row[5], telefono=row[6], genero=row[7])

@router.post("/", response_model=Personas, status_code=201)
async def create_item(item: Personas):
    cursor.execute("INSERT INTO TBL_PERSONAS (NUMERO_ID, NOMBRE, APELLIDO, FECHA_DE_NACIMIENTO, CORREO, TELEFONO, GENERO) VALUES (:numero_id, :nombre, :apellido, :fecha_de_nacimiento, :correo, :telefono, :genero)", {"numero_id": item.numero_id, "nombre": item.nombre, "apellido": item.apellido, "fecha_de_nacimiento": item.fecha_de_nacimiento, "correo": item.correo, "telefono": item.telefono, "genero": item.genero})
    connection.commit()
    return item

@router.put("/{id_persona}", response_model=Personas)
async def update_item(id_persona: int, item: Personas):
    cursor.execute("UPDATE TBL_PERSONAS SET NUMERO_ID = :numero_id, NOMBRE = :nombre, APELLIDO = :apellido, FECHA_DE_NACIMIENTO = :fecha_de_nacimiento, CORREO = :correo, TELEFONO = :telefono, GENERO = :genero WHERE ID_PERSONA = :id", {"numero_id": item.numero_id, "nombre": item.nombre, "apellido": item.apellido, "fecha_de_nacimiento": item.fecha_de_nacimiento, "correo": item.correo, "telefono": item.telefono, "genero": item.genero, "id": id_persona})
    connection.commit()
    cursor.execute("SELECT * FROM TBL_PERSONAS WHERE ID_PERSONA = :id", {"id": id_persona})
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Persona no encontrado")
    return Personas(id_persona=row[0], numero_id=[1], nombre=row[2], apellido=row[3], fecha_de_nacimiento=[4], correo=row[5], telefono=row[6], genero=row[7])

@router.delete("/{id_persona}")
async def delete_item(id_persona: int):
    cursor.execute("DELETE FROM TBL_PERSONAS WHERE ID_PERSONA = :id", {"id": id_persona})
    connection.commit()
    return {"message": "Persona eliminado correctamente"}


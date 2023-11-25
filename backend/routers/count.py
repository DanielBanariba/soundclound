# Se muestran las canciones con derechos de autor, si la cancion se reproduce, es porque ya esta registrado en la base de datos y no se puede volver a subir

from fastapi import APIRouter, HTTPException
#exporta la configuracion ya creada de la base de datos
from config import conectar_a_oracle
import cx_Oracle

configuracion = conectar_a_oracle()# Obtener la configuración de la base de datos
connection = cx_Oracle.connect(**configuracion)# Conectar a la base de datos
cursor = connection.cursor()

# Configuracion para la url y el mensaje personalizado
router = APIRouter(prefix="/count",  
                    tags=["count"], 
                    responses={404: {"message": "ID no encontrado"}})

@router.get("/")  # Reemplaza 'app' con 'router'
async def get_ids():
    print("Obteniendo IDs de canciones")
    cursor.execute('SELECT id FROM AUDIOS')
    results = cursor.fetchall()
    ids = [row[0] for row in results]
    return {"ids": ids}
# Se muestran las canciones con derechos de autor, si la cancion se reproduce, es porque ya esta registrado en la base de datos y no se puede volver a subir

from fastapi import APIRouter, HTTPException, status
#exporta la configuracion ya creada de la base de datos
from db.client import conectar_a_oracle
import cx_Oracle
import logging

logger = logging.getLogger("uvicorn.error")

configuracion = conectar_a_oracle()# Obtener la configuración de la base de datos
connection = cx_Oracle.connect(**configuracion)# Conectar a la base de datos
cursor = connection.cursor()

# Configuracion para la url y el mensaje personalizado
router = APIRouter(prefix="/count",  
                    tags=["count"], 
                    responses={404: {"message": "ID no encontrado"}})

@router.get("/", status_code=404) 
async def get_ids():
    try:
        print("Obteniendo IDs de canciones")
        cursor.execute('SELECT * FROM TBL_AUDIOS') #Obtener todos la informacion de la tabla AUDIOS, PERO! solo se necesita el ID, cambiar la consulta en dado caso de error, osea cambiar en * por ID
        results = cursor.fetchall()
        ids = [row[0] for row in results]
        return {"ids": ids}
    except:
        error_message = "No se ha encontrado ninguna cancion para mostrar en la pagina principal"
        logger.error(error_message)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_message)
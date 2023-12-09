from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from datetime import datetime
import cx_Oracle, os, sys
sys.path.append(os.path.join(os.getcwd(), 'backend'))#Obtener la ruta del directorio actual y concatenarla con el subdirectorio de los archivos de audio
from db.client import conectar_a_oracle

# Obtener la configuración de la base de datos
configuracion = conectar_a_oracle()

# Conectar a la base de datos
connection = cx_Oracle.connect(**configuracion)    
cursor = connection.cursor()

router = APIRouter(prefix="/generos", 
                    tags=["generos"], 
                    responses={404: {"message": "Genero no encontrado"}})

generos_list =  []


# -----------------------------------------GET----------------------------------------------------


# -----------------------------------------POST----------------------------------------------------
# Ya seria directamente iteractuando con la base de datos

# -----------------------------------------PUT----------------------------------------------------
# Ya seria directamente iteractuando con la base de datos

# ----------------------------------------DELETE----------------------------------------------------
# Ya seria directamente iteractuando con la base de datos


# -----------------------------------------FUNCIONES----------------------------------------------------

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from datetime import datetime
import cx_Oracle, os, sys
sys.path.append(os.path.join(os.getcwd(), 'backend'))#Obtener la ruta del directorio actual y concatenarla con el subdirectorio de los archivos de audio
from config import conectar_a_oracle

# Obtener la configuración de la base de datos
configuracion = conectar_a_oracle()

# Conectar a la base de datos
connection = cx_Oracle.connect(**configuracion)    
cursor = connection.cursor()

router = APIRouter(prefix="/users", 
                    tags=["users"], 
                    responses={404: {"message": "No encontrado"}})

class User(BaseModel):
    id_usuario: int
    id_tipo_usuario: int
    id_membresia: int
    id_artista: int
    id_oyente: int
    id_direccion: int
    nombre_usuario: str
    fecha_registro: datetime
    clave: str


users_list =  []


# -----------------------------------------GET----------------------------------------------------

# Ya seria directamente iteractuando con la base de datos
#inicio de la pagina principal
@router.get("/")
def get_users():
    try:
        cursor.execute("SELECT * FROM TBL_USUARIOS")
        return cursor.fetchall()
    except cx_Oracle.DatabaseError as e:
        return {"error": str(e)}


@router.get("/{id_usuario}")
def get_user(id_usuario: int):
    cursor.execute("SELECT * FROM TBL_USUARIOS WHERE ID_USUARIO = :id", {"id": id_usuario})
    user = cursor.fetchone()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return User(id_usuario=user[0], id_tipo_usuario=user[1], id_membresia=user[2], id_artista=user[3], id_oyente=user[4], id_direccion=user[5], nombre_usuario=user[6], fecha_registro=user[7], clave=user[8])


# Las operaciones GET son solo para obtener datos 
@router.get("/")
async def users():
    return users_list


@router.get("/user/{id}")# Path (Buscar en la documentacion)
        # el id tiene que ser si o si un entero
async def user(id: int):
    return search_user(id)


@router.get("/user/")# Query (Buscar en la documentacion)
        # el id tiene que ser si o si un entero
async def user(id: int):
    return search_user(id)


# -----------------------------------------POST----------------------------------------------------
# Ya seria directamente iteractuando con la base de datos
@router.post("/")
def create_user(user: User):
    try:
        cursor.execute(f"INSERT INTO TBL_USUARIOS VALUES ({user.id_usuario}, {user.id_tipo_usuario}, {user.id_membresia}, {user.id_artista}, {user.id_oyente}, {user.id_direccion}, '{user.nombre_usuario}', {user.fecha_registro}, '{user.clave}')")
        connection.commit()
        return {"message": "User created successfully"}
    except cx_Oracle.DatabaseError as e:
        return {"error": str(e)}

# con el metodo post lo que hacemos es crear nuevos usuarios
# osea creamos ID nuevas
@router.post("/user/", status_code=201)# Va a devolver el codigo correspondiente
async def user(user: User):
    if type(search_user(user.id)) == User:
        # El raise es como un return, pero que devuelve exclusivamente el codigo personalizado
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, 
                            detail="El usuario ya existe")# Errores personalizados

    # Si no, lo que hacemos es annadir un nuevo usuario
    users_list.routerend(user)
    return user


# -----------------------------------------PUT----------------------------------------------------
# Ya seria directamente iteractuando con la base de datos
@router.put("/{id_usuario}")
def update_user(id_usuario: int, user: User):
    try:
        cursor.execute(f"UPDATE TBL_USUARIOS SET ID_TIPO_USUARIO = {user.id_tipo_usuario}, ID_MEMBRESIA = {user.id_membresia}, ID_ARTISTA = {user.id_artista}, ID_OYENTE = {user.id_oyente}, ID_DIRECCION = {user.id_direccion}, NOMBRE_USUARIO = '{user.nombre_usuario}', FECHA_REGISTRO = {user.fecha_registro}, CLAVE = '{user.clave}' WHERE ID_USUARIO = {id_usuario}")
        connection.commit()
        return {"message": "User updated successfully"}
    except cx_Oracle.DatabaseError as e:
        return {"error": str(e)}

# Actualiza el usuario
@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"Error" : "No se ha actualizado el usuario"}
    else:
        return user


# ----------------------------------------DELETE----------------------------------------------------
# Ya seria directamente iteractuando con la base de datos
@router.delete("/{id_usuario}")
def delete_user(id_usuario: int):
    try:
        cursor.execute(f"DELETE FROM TBL_USUARIOS WHERE ID_USUARIO = {id_usuario}")
        connection.commit()
        return {"message": "User deleted successfully"}
    except cx_Oracle.DatabaseError as e:
        return {"error": str(e)}

@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]#del es una palabra reservada para eliminar 
            found = True

    if not found:
        return {"error" : "No se ha eliminado el usuario"}


# -----------------------------------------FUNCIONES----------------------------------------------------


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error" : "Usuario no encontrado"}
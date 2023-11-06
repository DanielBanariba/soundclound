from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/users", 
                    tags=["users"], 
                    responses={404: {"message": "No encontrado"}})

# Aqui podemos hacer varias clases para el proyecto de Soundcloud, como la clase:
# Artista, canciones, albumes, ect
class User(BaseModel):
# Estamos tipando los tipos de datos
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list =  [User(id=1, name="Daniel", surname="Barrientos", url="http://danielbanariba.com", age=25),
                User(id=2, name="Nina", surname="Barrientos", url="http://ninabanariba.com", age=15)]


# -----------------------------------------GET----------------------------------------------------


#inicio de la pagina principal
@router.get("/")
async def root():
    return "Hola Mundo, soy FastAPI"


# devuelve un jSON cuando se llama usersJason
@router.get("/usersJson")
async def usersJson():
    return [{"surname": "Daniel", "lasname": "Barrientos","url": "http://danielbanariba.com", "age": 25},
            {"surname": "Nina", "lasname": "Barrientos", "url": "http://ninabanariba.com", "age": 15}] 


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
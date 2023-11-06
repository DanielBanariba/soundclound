# Este archivo de codigo es basicamente la seguridad de nuestra API
# Lo que estamos haciendo es comprobar contraseña coincidan con su usuario

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm #Autenticacion

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool


class UserDB(User):
    password: str


# esta seria un ejemplo de una bases de datos no relacinal
users_db = {
    "danielbanariba":{
            "username": "daniel_banariba",
            "full_name": "daniel Barrientos Anariba",
            "email": "danielbanariba@gmail.com",
            "disable": False,
            "password": "123456"
    },
    "danielbanariba2":{
            "username": "daniel_banariba2",
            "full_name": "daniel Barrientos Anariba 2",
            "email": "danielbanariba2@gmail.com",
            "disable": False,
            "password": "654321"
    }
}

# buscasmos solo el nombre de usuarios
def search_user(username: str):
#Si username esta en la bases de datos, devuelveme el usuario
    if username in users_db:
        return UserDB(**users_db[username])


# Criterio de dependencia
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)    
    if not user: 
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Credenciales de autenticacion invalidas",
                headers={"www-authenticate": "Bearer"})
    return user 


#Estamos capturando usuario y contraseña
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="El usuario no es correcto")

    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="La contrasenna no es correcta")

    return{"access_token": user.username , "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
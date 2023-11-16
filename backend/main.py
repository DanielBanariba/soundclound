from fastapi import FastAPI, APIRouter
# importamos los archivos de la carpeta router
from routers import products, users, audio
# Nos permite exponer archivos estaticos como imagenes o en mi caso musica
from fastapi.staticfiles import StaticFiles 
# Devuelve el archivo de audio
from fastapi.responses import StreamingResponse
from os import getcwd, path
from conexion_oracle import conectar_a_oracle

app = FastAPI()

# Creamos un objeto APIRouter para envolver la lista de routers
router = APIRouter()

# Agregamos los routers a la ruta
router.include_router(products.router)
router.include_router(users.router)
router.include_router(audio.router)

# Incluimos el router en la aplicación FastAPI
app.include_router(router)

# Routers
#app.include_router([products.router, users.router, audio.router])

#Hecharle ojo a este pedazo de codigo
#app.mount("/static", StaticFiles(directory="static"), name="static")#Al momento de poner http://127.0.0.1:8000/static y el nombre de la carpeta y el nombre del archivo tiene que verse o exponerse


#url local: http://127.0.0.1:8000


@app.get("/")
async def root():
    return "Hola Mundo, soy FastAPI"


@app.get("/url")
async def url():
    return {"url": "http://www.danielbanariba.com"}


#---------------------PerPlesity------------------------

app.mount("/audios", StaticFiles(directory="audios"), name="audios")

if __name__ == "__main__":
    crear_tabla_audio()
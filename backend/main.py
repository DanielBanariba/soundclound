from fastapi import FastAPI, APIRouter, Request
# importamos los archivos de la carpeta router
from routers import products, users, audio, reproducir
from fastapi.responses import FileResponse
# Nos permite exponer archivos estaticos como archivos HTML
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Creamos un objeto APIRouter para envolver la lista de routers
router = APIRouter()

# Agregamos los routers a la ruta
router.include_router(products.router)
router.include_router(users.router)
router.include_router(audio.router)
router.include_router(reproducir.router)

# Incluimos el router en la aplicación FastAPI
app.include_router(router)

# Routers
#app.include_router([products.router, users.router, audio.router])

#Va a reproducir los auidos que tengamos en la carpeta audios, http://127.0.0.1:8000/audios/<<El Nombre de la cancion>>
app.mount("/audios", StaticFiles(directory="audios"), name="audios")#Al momento de poner http://127.0.0.1:8000/static y el nombre de la carpeta y el nombre del archivo tiene que verse o exponerse
app.mount("/static", StaticFiles(directory="static"), name="static")


#url local: http://127.0.0.1:8000


@app.get("/")
async def root(request: Request):
    return FileResponse('static/templates/index.html')
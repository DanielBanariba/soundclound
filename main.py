from fastapi import FastAPI, APIRouter, Request, Response
# importamos los archivos de la carpeta router
from backend.routers import users, audio, reproducir, copyright, count, artista, canciones, facturacion_pagos, personas
from fastapi.responses import FileResponse
# Nos permite exponer archivos estaticos como archivos HTML
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Creamos un objeto APIRouter para envolver la lista de routers
router = APIRouter()

# Agregamos los routers a la ruta
router.include_router(artista.router)
router.include_router(audio.router)
router.include_router(canciones.router)
router.include_router(facturacion_pagos.router)
router.include_router(personas.router)
router.include_router(users.router)
router.include_router(copyright.router)
router.include_router(count.router)
router.include_router(reproducir.router)#127.0.0.1:8000/reproducir/<<El Nombre de la cancion>>

# Incluimos el router en la aplicación FastAPI
app.include_router(router)

# Routers
#app.include_router([products.router, users.router, audio.router])

#Va a reproducir los auidos que tengamos en la carpeta audios, http://127.0.0.1:8000/audios/<<El Nombre de la cancion>>
app.mount("/audios", StaticFiles(directory="backend/audios"), name="audios")#Al momento de poner http://127.0.0.1:8000/static y el nombre de la carpeta y el nombre del archivo tiene que verse o exponerse
app.mount("/static", StaticFiles(directory="backend/static"), name="static")


#url local: http://127.0.0.1:8000


@app.get("/")
async def root(request: Request):
    return FileResponse('backend/static/templates/index.html')

#Esto es para que no salga el error de "Get /favicon.ico HTTP/1.1" 404 Not Found
@app.get("/favicon.ico")
async def favicon():
    return Response(content="", media_type="image/x-icon")
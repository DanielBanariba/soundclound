from fastapi import FastAPI
# importamos los archivos de la carpeta router
from routers import products, users 
# Nos permite exponer archivos estaticos como imagenes o en mi caso musica
from fastapi.staticfiles import StaticFiles 


app = FastAPI()

# Routers
app.include_router(products.router)#que es el ".router"? es lo que hemos definido dentro del archivo router
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")#Al momento de poner http://127.0.0.1:8000/static y el nombre de la carpeta y el nombre del archivo tiene que verse o exponerse


#url local: http://127.0.0.1:8000


@app.get("/")
async def root():
    return "Hola Mundo, soy FastAPI"


@app.get("/url")
async def url():
    return {"url": "http://www.danielbanariba.com"}

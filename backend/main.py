from fastapi import FastAPI, APIRouter, Request, Response
# importamos los archivos de la carpeta router
from routers import products, users, audio, reproducir, copyright, count
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
router.include_router(copyright.router)
router.include_router(count.router)
router.include_router(reproducir.router)#127.0.0.1:8000/reproducir/<<El Nombre de la cancion>>

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

#Esto es para que no salga el error de "Get /favicon.ico HTTP/1.1" 404 Not Found
@app.get("/favicon.ico")
async def favicon():
    return Response(content="", media_type="image/x-icon")

""""
1. **Validación de datos**: Podrías usar Pydantic para validar los datos de entrada de tus endpoints. Por ejemplo, si tienes un endpoint que acepta un ID de producto, podrías usar un modelo Pydantic para asegurarte de que el ID es un número entero.

2. **Autenticación y autorización**: Si tu API necesita ser segura, podrías agregar autenticación y autorización. FastAPI tiene varias opciones para esto, incluyendo OAuth2 y JWT.

3. **Pruebas unitarias**: Podrías escribir pruebas unitarias para tus endpoints para asegurarte de que funcionan como se espera.

4. **Documentación**: FastAPI genera automáticamente una documentación interactiva para tu API, pero podrías personalizarla aún más. Por ejemplo, podrías agregar descripciones a tus modelos Pydantic y endpoints para explicar qué hacen.

5. **Manejo de errores**: Podrías agregar más manejo de errores a tu aplicación. FastAPI te permite definir manejadores de excepciones que pueden capturar errores y devolver respuestas personalizadas.

6. **Registros (Logging)**: Podrías agregar registros a tu aplicación para ayudarte a depurar problemas. Python tiene un módulo de registro incorporado que puedes usar para esto.

7. **Base de datos**: Si aún no lo has hecho, podrías conectar tu API a una base de datos. FastAPI es compatible con cualquier base de datos que tenga un controlador Python, incluyendo SQL y NoSQL.
"""
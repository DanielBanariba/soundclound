<div align="center">
  <h1 align="center">Soundcloud</a></h1>
</div>

<div align="center">
  <img align="center" src="backend\static\imagenes\soundcloud-icon-2048x888-k4c33ssc.png" alt="soundcloud" width="50%">
</div>
<br>

Ir a la documentacion para la creacion de un entorno virtual
https://docs.python.org/3/library/venv.html

Crear un entorno virtual
 ```sh
python -m venv /path/to/new/virtual/environment
```
 ```sh
python -m venv env
```

Acceder a la carpeta env, scripts 
```sh
cd env/Scripts
```

y por ultimo activarlo, y ya estaremos en el entorno virtual
```sh
.\activate.ps1
```

Instalar las dependencia necesarias:

En un solo comando: 
```sh
pip install fastapi "uvicorn[standard]" oracledb cx_Oracle python-multipart jinja2 matplotlib
``` 
  
Oh uno por uno (Si es que tuvo problemas en instalarlo de un solo):
```sh
pip install fastapi
```
```sh
pip install "uvicorn[standard]"
```
```sh
pip install oracledb
```
```sh
pip install cx_Oracle
```
```sh
pip install python-multipart
```
```sh
pip install jinja2
```
```sh
pip install matplotlib
```

  
  Nota: Si le sale error al momento de querer instalar oracledb, le recomiendo que instale Microsoft C++ Build Tools le dejare un link para su facil acceso. 
   >Link: https://visualstudio.microsoft.com/es/visual-cpp-build-tools/

Levantar el servidor
```sh
python -m uvicorn main:app –reload
```
  
Si va a levatar el servidor desde visual studio code
```sh
uvicorn main:app
```

Ir a la documentación: 
  Con Swagger: -127.0.0.1:8000/docs  
  Con Redocly: -127.0.0.1:8000/recdo
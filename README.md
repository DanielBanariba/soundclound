# soundclound

Ir a la documentacion para la creacion de un entorno virtual
https://docs.python.org/3/library/venv.html

Crear un entorno virtual
  >python -m venv /path/to/new/virtual/environment

O tambien con el comando
  >python -m venv env

Acceder a la carpeta venv, scripts y por ultimo activarlo, y ya estaremos en el entorno virtual
  >cd venv/env/Scripts/Activate.ps1

Instalar las dependencia necesarias
  - pip install fastapi
  - pip install "uvicorn[standard]"
  - pip install oracledb
  - pip install cx_Oracle
  - pip install python-multipart
  - pip install os


  
  Nota: Si le sale error al momento de querer instalar oracledb, le recomiendo que instale Microsoft C++ Build Tools le dejare un link para su facil acceso. 
   >Link: https://visualstudio.microsoft.com/es/visual-cpp-build-tools/

Levantar el servidor
  - python -m uvicorn main:app –reload
  
Si va a levatar el servidor desde visual studio code
  - uvicorn main:app

Ir a la documentación: 
  Con Swagger: -127.0.0.1:8000/docs  
  Con Redocly: -127.0.0.1:8000/recdo
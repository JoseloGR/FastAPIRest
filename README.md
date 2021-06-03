# API Rest

El backend se desarrolló utilizando el Framework FastAPI, usa Python como lenguaje de programación. Se debe usar un virtual environment para correrlo.

## Instalación y ejecución de BackEnd

Para este proyecto recomiendo utilizar `pipenv`. Previamente debes tener instalado `Python` y `pipenv`. A continuación puedes revisar la documentación de `pipenv` por cualquier duda sobre su instalación.

- [PipEnv](https://pipenv-es.readthedocs.io/es/latest)
- Python versión mínima `3.7.7`
- pip versión `21.1.2`

Para correr el servidor backend en localhost debes ejecutar los siguientes comandos:

```bash
cd FastAPIRest/
pipenv shell
pipenv install
uvicorn main:app --reload
```

Se levantará un servidor local sobre el puerto 8000

Para poder ver la documentación de los endpoints deberás acceder a `http://localhost:8000/docs`

Una vez que se tiene corriendo el servidor backend se puede abrir la aplicación web


Si se desea utilizar un virtual environment con virtualenv podrás usar el archivo requirements.txt
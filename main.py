from fastapi import (
  FastAPI,
  status
)
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import (
  CLIENTS,
  USUARIOS,
  VENTAS,
  CAT_EQUIPOS,
  CAT_USUARIOS
)

app = FastAPI()

origins = ['*']

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def home():
  return {'version': '1.0.0'}


@app.get("/clientes/{id}")
def get_client_by_id(id: int):
  client = list(filter(lambda x: x.get("id", 0) == id, CLIENTS))
  response = {}
  status_code = status.HTTP_404_NOT_FOUND
  if client:
    response = client[0]
    status_code = status.HTTP_200_OK
  return JSONResponse(
    status_code=status_code,
    content=response
  )

@app.get("/clientes")
def get_clients():
  return JSONResponse(
    status_code=status.HTTP_200_OK,
    content=CLIENTS
  )

@app.get("/usuarios/{id}")
def get_user_by_id(id: int):
  user = list(filter(lambda x: x.get("id", 0) == id, USUARIOS))
  response = {}
  status_code = status.HTTP_404_NOT_FOUND
  if user:
    response = user[0]
    status_code = status.HTTP_200_OK
  return JSONResponse(
    status_code=status_code,
    content=response
  )

@app.get("/usuarios")
def get_users():
  return JSONResponse(
    status_code=status.HTTP_200_OK,
    content=USUARIOS
  )

@app.get("/ventas/equipo/{id}")
def get_sales_by_team(id: int):
  sales = list(filter(lambda x: x.get("equipo_id", 0) == id, VENTAS))
  status_code = status.HTTP_200_OK if sales else status.HTTP_404_NOT_FOUND
  return JSONResponse(
    status_code=status_code,
    content=sales
  )

@app.get("/ventas/usuario/{id}")
def get_sales_by_user(id: int):
  sales = list(filter(lambda x: x.get("usuario_id", 0) == id, VENTAS))
  status_code = status.HTTP_200_OK if sales else status.HTTP_404_NOT_FOUND
  return JSONResponse(
    status_code=status_code,
    content=sales
  )

@app.get("/catalogo/{nombre}")
def get_catalog(nombre: str):
  options = {
    'equipos': CAT_EQUIPOS,
    'usuarios': CAT_USUARIOS
  }
  catalogs = options.get(nombre, [])
  return JSONResponse(
    status_code=status.HTTP_200_OK,
    content=catalogs
  )

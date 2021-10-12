from db.autor_db import AutorDB
#from db.autor_db import get_autor
#from db.autor_db import database_autores
from db.resena_db import ResenaDB
from fastapi import FastAPI, Depends
from fastapi import HTTPException
from routers.router_autor import router as router_autor
from routers.router_pelicula import router as router_pelicula
from routers.router_resena import router as router_resena

api = FastAPI()

api.include_router(router_autor)
api.include_router(router_pelicula)
api.include_router(router_resena)


from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8080", "https://cinencuadre.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


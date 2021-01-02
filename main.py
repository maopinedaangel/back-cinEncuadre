from db.autor_db import AutorDB
#from db.autor_db import get_autor
#from db.autor_db import database_autores
from db.resena_db import ResenaDB
from fastapi import FastAPI, Depends
from fastapi import HTTPException
from routers.router_autor import router as router_autor

api = FastAPI()

api.include_router(router_autor)


from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8080",
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


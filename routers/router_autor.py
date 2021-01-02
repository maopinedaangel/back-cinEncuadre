from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.autor_db import AutorDB
#from db.autor_db import get_autor

from models.autor_models import AutorIn, AutorOut
#from db.autor_db import database_autores


router = APIRouter()

'''
@router.get("/autor")
async def mostrar_autor(username: str):
    autor = get_autor(username)
    if autor == None:
        raise HTTPException(status_code=404, detail="No se reconoce el username.")
    return autor

@router.get("/autores")
async def mostrar_autores():
    return database_autores
'''


@router.post("/autor/auth/")
async def auth_autor(autor_in: AutorIn, db: Session = Depends(get_db)):
    autor_in_db = db.query(AutorDB).get(autor_in.username)

    if autor_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe.")

    if autor_in_db.password != autor_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticación.")

    return {"Autenticado" : True}


@router.get("/autor/perfil/{username}", response_model=AutorOut)
async def get_perfil(username: str, db: Session = Depends(get_db)):

    autor_in_db = db.query(AutorDB).get(username)

    if autor_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    return autor_in_db



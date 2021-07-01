from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db
from db.pelicula_db import PeliculaDB
from models.pelicula_models import PeliculaIn, PeliculaOut


router = APIRouter()

@router.get("/peliculas/", response_model=List[PeliculaOut])
async def mostrar_peliculas(db: Session = Depends(get_db)):
    peliculas = db.query(PeliculaDB).all()
    return peliculas

@router.post("/pelicula/save/")
async def auth_autor(pelicula_in: PeliculaIn, db: Session = Depends(get_db)):
    autor_in_db = db.query(AutorDB).get(autor_in.username)

    if autor_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe.")

    if autor_in_db.password != autor_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticación.")

    return {"Autenticado" : True}
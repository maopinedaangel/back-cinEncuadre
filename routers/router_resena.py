from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import sqlalchemy as sql
from sqlalchemy import desc, func, distinct

from db.db_connection import get_db
from db.pelicula_db import PeliculaDB
from db.resena_db import ResenaDB
from models.pelicula_models import PeliculaIn, PeliculaOut
from models.resena_models import ResenaIn, ResenaOut
from models.resena_models import PeliIn, ArticuloIn
import datetime

router = APIRouter()

@router.post("/resena/save")
async def save_resena(resena_in: ResenaIn, db: Session = Depends(get_db)):

    peli = PeliculaDB(**resena_in.peli_in.dict())

    db.add(peli)
    db.commit()
    db.refresh(peli)
    
    articulo = ResenaDB(**resena_in.articulo_in.dict(), id_pelicula = peli.id)

    db.add(articulo)
    db.commit()
    db.refresh(articulo)  

    return {"mensaje" : "Reseña guardada exitosamente."}
  

#@router.get("/resenas/", response_model=List[PeliculaOut])
@router.get("/resenas")
#async def get_resenas (db: Session = Depends(get_db)):
async def get_resenas (director: Optional[str]=None, anno: Optional[int]=None, pais: Optional[str]=None, username: Optional[str]= None, categoria: Optional[str]=None, criterio: Optional[str]=None, db: Session = Depends(get_db)):    
    mi_query = db.query(ResenaDB, PeliculaDB).join(PeliculaDB)    
    if username != None:
        mi_query = mi_query.filter(ResenaDB.username==username)
    if pais != None:
        mi_query = mi_query.filter(PeliculaDB.pais==pais)
    if anno != None:
        mi_query = mi_query.filter(PeliculaDB.anno==anno) 
    if categoria != None:
        mi_query = mi_query.filter(ResenaDB.categoria==categoria)
    if director != None:
        mi_query = mi_query.filter(PeliculaDB.director==director)                      
    #pelis = [r.__dict__ for r in mi_query.all()]
    #mi_query = mi_query.order_by(PeliculaDB.anno)
    #criterio = "fecha"
    if criterio == "anno":
        pelis = mi_query.order_by(PeliculaDB.anno).all() 
    elif criterio == "director":
        pelis = mi_query.order_by(PeliculaDB.director).all()  
    elif criterio == "username":
        pelis = mi_query.order_by(ResenaDB.username).all() 
    elif criterio == "pais":
        pelis = mi_query.order_by(PeliculaDB.pais).all()
    elif criterio == "categoria":
        pelis = mi_query.order_by(ResenaDB.categoria).all()
    elif criterio == "titulo":
        pelis = mi_query.order_by(PeliculaDB.titulo).all()    
    else:
        pelis = mi_query.order_by(desc(ResenaDB.id)).all()                                
    #pelis = mi_query.order_by(desc(PeliculaDB.id)).all()
    return pelis


@router.get("/filtro")
async def get_filtro (db: Session = Depends(get_db)):
    user="andres"
    #result = db.query(ResenaDB).join(PeliculaDB).filter(ResenaDB.id_pelicula==1).all() 
    result = db.query(ResenaDB, PeliculaDB).join(PeliculaDB).filter(ResenaDB.username==user).all()      
    return result


@router.get("/peliculas/pais")
async def get_peliculas (db: Session = Depends(get_db)):
    #result = db.query(ResenaDB).join(PeliculaDB).filter(ResenaDB.id_pelicula==1).all() 
    result = db.query(PeliculaDB).filter(PeliculaDB.pais=="Estados Unidos").all()      
    return result

#@router.get("/resena", response_model=ResenaOut)
@router.get("/resena")
async def get_resena(id: int, db: Session = Depends(get_db)):
  
    resena_in_db = db.query(ResenaDB, PeliculaDB).join(PeliculaDB).filter(ResenaDB.id==id).first()   
    if resena_in_db == None:
        raise HTTPException(status_code=404, detail="No se encontraron datos.")

    return resena_in_db

@router.get("/categorias")
async def get_categorias(db: Session = Depends(get_db)):
    lista_categorias = db.query(func.distinct(ResenaDB.categoria)).all() 
    lista = [] 
    for item in lista_categorias:
        lista.append(item[0]) 
    return lista
from pydantic import BaseModel
from datetime import datetime


class PeliIn(BaseModel):
    titulo: str
    director: str
    anno: int
    pais: str   

class ArticuloIn(BaseModel):
    username: str
    categoria: str
    titulo: str
    texto: str
    imagen: str
    status: bool    

class ResenaIn(BaseModel):
    peli_in: PeliIn
    articulo_in: ArticuloIn

    ''' 
class ResenaIn(BaseModel): 

    username: str
    titulo: str    
    id_pelicula: int
    director: str
    anno: str
    pais: str
    categoria: str
    username: str      
    id_pelicula: str
    texto: str 
    imagen: str
    status: bool
    '''

class ResenaOut(BaseModel):
    titulo: str
    username: str
    pelicula: str
    fecha: str
    categoria: str
    texto: str 
    imagen: str


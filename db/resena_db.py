from typing import Dict
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from db.db_connection import Base, engine
import datetime

'''
class ResenaDB(BaseModel):
    id_resena: int
    username: str
    id_pelicula: str
    fecha: datetime.date
    titulo: str
    texto: str
    resumen: str
    categoria: str
    status: bool
'''

class ResenaDB(Base):
    __tablename__ = "resena"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey("autor.username"))
    id_pelicula = Column(Integer, ForeignKey("pelicula.id"))
    fecha = Column(DateTime, default=datetime.datetime.utcnow)
    titulo = Column(String)
    texto = Column(String)
    categoria = Column(String)
    imagen = Column(String)
    status = Column(Boolean, default=True)

'''
database_resena = {
    "1": ResenaDB(id_resena="1", username="fred", id_pelicula="1", fecha="2020-12-25", titulo="La loca historia del mundo", texto="Película de Mel Brooks.", resumen="Película de Mel Brooks.", categoria="RieteCinEncuadre", status=True),
    "2": ResenaDB(id_resena="2", username="juan", id_pelicula="2", fecha="2020-12-26", titulo="Sonrisas de una noche de verano", texto="Película de Ingmar Bergman.", resumen="Película de Ingmar Bergman.", categoria="Efeméride", status=True),
    "3": ResenaDB(id_resena="3", username="liz", id_pelicula="3", fecha="2020-12-27", titulo="Todo sobre mi madre", texto="Película de Pedro Almodóvar.", resumen="Película de Pedro Almodóvar.", categoria="Desencuadrando a Almodóvar", status=True),        
}                       
'''
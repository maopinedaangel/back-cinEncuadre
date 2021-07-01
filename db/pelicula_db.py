from typing import Dict
from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine

class PeliculaDB(Base):
    __tablename__ = "pelicula"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    director = Column(String)
    anno = Column(Integer)
    pais = Column(String)


Base.metadata.create_all(bind=engine)
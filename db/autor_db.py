from typing import Dict
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from db.db_connection import Base, engine

'''
class AutorDB(BaseModel):
    username: str
    nombre: str
    apellido: str
    perfil: str
    email: str
    password: str
    status: bool
'''

class AutorDB(Base):
    __tablename__ = "autor"

    username = Column(String, primary_key=True, unique=True)
    nombre = Column(String)
    apellido = Column(String)
    perfil = Column(String)
    foto = Column(String)
    email = Column(String)
    password = Column(String)
    status = Column(Boolean)

Base.metadata.create_all(bind=engine)

'''
database_autores = {
    "fred": AutorDB(username="fred", nombre="Freddy", apellido="Jiménez", perfil="Diseñador gráfico.", email="fredjimer@gmail.com", password="fred123", status=True),
    "juan": AutorDB(username="juan", nombre="Juan David", apellido="Suárez Ceballos", perfil="Sociólogo e investigador.", email="juasucine@gmail.com", password="juan123", status=True),
    "liz": AutorDB(username="liz", nombre="Liz Evelyn", apellido="Echavarría", perfil="Socióloga y cinéfila.", email="lizevelynechavarria.h@gmail.com", password="liz123", status=True), 
    "andres": AutorDB(username="andres", nombre="Andrés", apellido="Hernández", perfil="Cinéfilo.", email="ccioran@hotmail.com", password="andres123", status=True),
    "mao": AutorDB(username="mao", nombre="Mauricio", apellido="Pineda Angel", perfil="Cinéfilo.", email="ingmauriciopinedar@gmail.com", password="mao123", status=True),
    "adriana": AutorDB(username="adriana", nombre="Adriana Patricia", apellido="Zamudio Barrientos", perfil="Cinéfila.", email="odonatazamudio@gmail.com", password="adriana123", status=True),
    "luz": AutorDB(username="luz", nombre="Luz Dary", apellido="Mejía", perfil="Cinéfila", email="luzdary_mejia@yahoo.es", password="luz123", status=True)
}                       
'''

'''
def get_autor(username: str):
    if username in database_autores:
        return database_autores[username]
    else:
        return None
'''
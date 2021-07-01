from pydantic import BaseModel

class AutorIn(BaseModel):
    username: str
    password: str

class AutorOut(BaseModel):
    username: str
    nombre: str
    apellido: str
    perfil: str
    foto: str
    tipo: str

    class Config:
        orm_mode = True
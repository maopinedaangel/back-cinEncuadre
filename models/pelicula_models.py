from pydantic import BaseModel

class PeliculaIn(BaseModel):
    titulo: str

class PeliculaOut(BaseModel):
    titulo: str
    director: str
    anno: int
    pais: str

    class Config:
        orm_mode = True
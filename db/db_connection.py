from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#DATABASE_URL = "postgresql://user:password@host:port/name_db"
#DATABASE_URL = "postgresql://postgres:Admin123@localhost:5432/cinencuadre"
DATABASE_URL = os.environ['DATABASE_URL']
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
Base.metadata.schema = "web_cinencuadre"

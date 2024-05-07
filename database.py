from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

URL_DATABASE='sqlite:///./pizzadb.db'

engine=create_engine(URL_DATABASE)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

class Base(DeclarativeBase):
    pass


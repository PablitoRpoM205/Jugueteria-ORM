from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entities.base import Base, declarative_base

from database.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy import Column, Integer, ForeignKey
from database.connection import Base

class Didactico(Base):
    __tablename__ = "didacticos"

    id = Column(Integer, primary_key=True)
    juguete_id = Column(Integer, ForeignKey("juguetes.id"), unique=True)
    edad_minima = Column(Integer, default=3)

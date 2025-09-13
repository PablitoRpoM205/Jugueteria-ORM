from sqlalchemy import Column, Integer, String, Float
from database.connection import Base

class Juguete(Base):
    __tablename__ = "juguetes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    tipo = Column(String, nullable=False)

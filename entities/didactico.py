from sqlalchemy import Column, Integer, String
from entities.base import Base

class Didactico(Base):
    __tablename__ = 'didacticos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Integer)
    stock = Column(Integer)
    tipo = Column(String, default="didactico")  # Tipo específico para juguetes didácticos

    def __repr__(self):
        return f"<Didactico(nombre={self.nombre}, precio={self.precio}, stock={self.stock})>"
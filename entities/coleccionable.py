from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from entities.base import Base

class Coleccionable(Base):
    __tablename__ = 'coleccionables'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Integer)
    stock = Column(Integer)
    tipo = Column(String, default='coleccionable')
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))

    usuario = relationship("Usuario", back_populates="coleccionables")
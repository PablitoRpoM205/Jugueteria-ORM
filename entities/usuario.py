from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from entities.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False)
    contrasena = Column(String, nullable=False)

    ventas = relationship("Venta", back_populates="usuario")

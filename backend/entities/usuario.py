from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from entities.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False)
    contrasena = Column(String, nullable=False)
    es_admin = Column(Boolean, default=False)

    ventas = relationship("Venta", back_populates="usuario")
    juguetes = relationship("Juguete", back_populates="usuario")
    inventario = relationship("Inventario", back_populates="usuario")

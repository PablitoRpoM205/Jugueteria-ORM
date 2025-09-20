"""
Tabla juguetes. 'tipo' discrimina el subtipo (electronico, didactico, coleccionable).
Todas las tablas usan UUID como id primario.
"""

import uuid
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.connection import Base
from entities.base import AuditMixin


class Juguete(Base, AuditMixin):
    """
    Tabla juguetes. 'tipo' discrimina el subtipo (electronico, didactico, coleccionable).
    Todas las tablas usan UUID como id primario.
    """

    __tablename__ = "juguetes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(200), nullable=False, index=True)
    descripcion = Column(String(255), nullable=True)
    tipo = Column(String(50), nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    es_edicion_limitada = Column(Boolean, default=False)

    ventas = relationship(
        "Venta", back_populates="juguete", cascade="all, delete-orphan"
    )
    inventarios = relationship(
        "Inventario", back_populates="juguete", cascade="all, delete-orphan"
    )
    coleccionable = relationship(
        "Coleccionable",
        uselist=False,
        back_populates="juguete",
        cascade="all, delete-orphan",
    )
    didactico = relationship(
        "Didactico",
        uselist=False,
        back_populates="juguete",
        cascade="all, delete-orphan",
    )
    electronico = relationship(
        "Electronico",
        uselist=False,
        back_populates="juguete",
        cascade="all, delete-orphan",
    )

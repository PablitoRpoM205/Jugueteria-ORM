"""
Entidad Usuario.
Modelo para almacenar credenciales y datos básicos de usuario.
"""

import uuid
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.connection import Base
from entities.base import AuditMixin


class Usuario(Base, AuditMixin):
    """
    Tabla usuarios.
    """

    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
    nombre_usuario = Column(String(50), unique=True, index=True, nullable=False)
    correo = Column(String(150), unique=True, index=True, nullable=False)
    contraseña_hash = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=False)
    es_admin = Column(Boolean, default=False)

    ventas = relationship(
        "Venta", back_populates="usuario", cascade="all, delete-orphan"
    )
    inventarios = relationship(
        "Inventario", back_populates="usuario", cascade="all, delete-orphan"
    )

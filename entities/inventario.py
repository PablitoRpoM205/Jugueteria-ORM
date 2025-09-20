"""
Entidad Inventario: relaciona usuario y juguete con cantidad.
"""

import uuid
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.connection import Base
from entities.base import AuditMixin


class Inventario(Base, AuditMixin):
    """
    Tabla inventario que almacena la cantidad disponible de un juguete para un usuario (propietario).
    """

    __tablename__ = "inventario"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    usuario_id = Column(
        UUID(as_uuid=True),
        ForeignKey("usuarios.id", ondelete="CASCADE"),
        nullable=False,
    )
    juguete_id = Column(
        UUID(as_uuid=True),
        ForeignKey("juguetes.id", ondelete="CASCADE"),
        nullable=False,
    )
    cantidad = Column(Integer, nullable=False, default=0)

    usuario = relationship("Usuario", back_populates="inventarios")
    juguete = relationship("Juguete", back_populates="inventarios")

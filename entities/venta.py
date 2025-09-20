"""
Entidad Venta: registro de ventas realizadas.
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, Float, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.connection import Base
from entities.base import AuditMixin


class Venta(Base, AuditMixin):
    """
    Tabla ventas que registra cada transacción.
    """

    __tablename__ = "ventas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    usuario_id_vendio = Column(
        UUID(as_uuid=True),
        ForeignKey("usuarios.id", ondelete="CASCADE"),
        nullable=False,
    )
    juguete_id = Column(
        UUID(as_uuid=True),
        ForeignKey("juguetes.id", ondelete="CASCADE"),
        nullable=False,
    )
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    fecha_venta = Column(DateTime, default=datetime.utcnow, nullable=False)

    usuario = relationship("Usuario", back_populates="ventas")
    juguete = relationship("Juguete", back_populates="ventas")

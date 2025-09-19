"""
Entidad Electronico: subtipo de juguete con datos adicionales.
Relación 1:1 con juguetes mediante juguete_id.
"""

import uuid
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database.connection import Base
from entities.base import AuditMixin


class Electronico(Base, AuditMixin):
    """
    Tabla electronicos con referencia al juguete padre.
    """

    __tablename__ = "electronicos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    juguete_id = Column(
        UUID(as_uuid=True), ForeignKey("juguetes.id"), nullable=False, unique=True
    )
    garantia_meses = Column(Integer, nullable=False, default=12)

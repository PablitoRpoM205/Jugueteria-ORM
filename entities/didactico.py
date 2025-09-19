"""
Entidad Didactico: subtipo de juguete con datos adicionales.
"""

import uuid
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database.connection import Base
from entities.base import AuditMixin


class Didactico(Base, AuditMixin):
    """
    Tabla didacticos con referencia al juguete padre.
    """

    __tablename__ = "didacticos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    juguete_id = Column(
        UUID(as_uuid=True), ForeignKey("juguetes.id"), nullable=False, unique=True
    )
    edad_minima = Column(Integer, nullable=False, default=3)

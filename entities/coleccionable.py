"""
Entidad Coleccionable: subtipo de juguete con datos adicionales.
"""

import uuid
from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.connection import Base
from entities.base import AuditMixin


class Coleccionable(Base, AuditMixin):
    """
    Tabla coleccionables con referencia al juguete padre.
    """

    __tablename__ = "coleccionables"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    juguete_id = Column(
        UUID(as_uuid=True),
        ForeignKey("juguetes.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )
    edicion_limitada = Column(Boolean, nullable=False, default=False)
    juguete = relationship("Juguete", back_populates="coleccionable", uselist=False)

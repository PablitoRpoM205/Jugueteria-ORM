"""
Mixin y utilidades base para entidades.
Define el mixin de auditoría que se incluirá en todas las tablas.
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class AuditMixin:
    """
    Agrega los campos de auditoría obligatorios:
    - id_usuario_creacion: UUID del usuario que creó el registro
    - id_usuario_edicion: UUID del último usuario que editó el registro
    - fecha_creacion: timestamp de creación
    - fecha_edicion: timestamp de la última actualización
    """

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

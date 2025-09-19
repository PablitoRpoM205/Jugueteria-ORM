import uuid
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AuditMixin:
    """Campos de auditoría obligatorios para todas las entidades."""

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=False)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())


class Usuario(Base, AuditMixin):
    """Entidad usuario del sistema."""

    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    rol = Column(String(50), nullable=False)

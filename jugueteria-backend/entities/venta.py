from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from entities.base import Base


class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    juguete_id = Column(Integer, ForeignKey("juguetes.id"))
    cantidad = Column(Integer, nullable=False)

    usuario = relationship("Usuario", back_populates="ventas")
    juguete = relationship("Juguete")

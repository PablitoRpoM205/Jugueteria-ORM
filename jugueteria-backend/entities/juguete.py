from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from entities.base import Base


class Juguete(Base):
    __tablename__ = "juguetes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    tipo = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario")
    inventario = relationship(
        "Inventario",
        back_populates="juguete",
        uselist=False,
        cascade="all, delete-orphan",
    )

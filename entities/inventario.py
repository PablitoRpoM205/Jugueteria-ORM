from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from entities.base import Base


class Inventario(Base):
    __tablename__ = "inventarios"

    id = Column(Integer, primary_key=True, index=True)
    juguete_id = Column(Integer, ForeignKey("juguetes.id"))
    usuario_id = Column(
        Integer,
        ForeignKey(
            "usuarios.id",
        ),
    )
    cantidad = Column(Integer, nullable=False)

    juguete = relationship("Juguete", back_populates="inventario")
    usuario = relationship("Usuario", back_populates="inventario")

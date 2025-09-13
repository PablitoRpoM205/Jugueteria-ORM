from sqlalchemy import Column, Integer, ForeignKey
from database.connection import Base

class Inventario(Base):
    __tablename__ = "inventario"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    juguete_id = Column(Integer, ForeignKey("juguetes.id"), nullable=False)
    cantidad = Column(Integer, default=0)

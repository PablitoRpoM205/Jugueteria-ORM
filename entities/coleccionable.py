from sqlalchemy import Column, Integer, ForeignKey, Boolean
from database.connection import Base

class Coleccionable(Base):
    __tablename__ = "coleccionables"

    id = Column(Integer, primary_key=True)
    juguete_id = Column(Integer, ForeignKey("juguetes.id"), unique=True)
    edicion_limitada = Column(Boolean, default=False)

from sqlalchemy import Column, Integer, ForeignKey
from database.connection import Base

class Electronico(Base):
    __tablename__ = "electronicos"

    id = Column(Integer, primary_key=True)
    juguete_id = Column(Integer, ForeignKey("juguetes.id"), unique=True)
    garantia_meses = Column(Integer, default=12)

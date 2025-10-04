from sqlalchemy.orm import Session
from entities.inventario import Inventario


def obtener_inventario(db: Session):
    return db.query(Inventario).all()


def actualizar_inventario(db: Session, inventario_id: int, inventario_data: dict):
    inventario = db.query(Inventario).filter(Inventario.id == inventario_id).first()
    if inventario:
        for key, value in inventario_data.items():
            setattr(inventario, key, value)
        db.commit()
        db.refresh(inventario)
    return inventario

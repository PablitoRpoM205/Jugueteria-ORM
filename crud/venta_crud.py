from sqlalchemy.orm import Session
from entities.venta import Venta
from database.connection import SessionLocal

def crear_venta(db: Session, id_juguete: int, cantidad: int, id_usuario: int) -> Venta:
    nueva_venta = Venta(id_juguete=id_juguete, cantidad=cantidad, id_usuario=id_usuario)
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

def obtener_ventas(db: Session):
    return db.query(Venta).all()

def obtener_venta_por_id(db: Session, venta_id: int) -> Venta:
    return db.query(Venta).filter(Venta.id == venta_id).first()

def actualizar_venta(db: Session, venta_id: int, cantidad: int) -> Venta:
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if venta:
        venta.cantidad = cantidad
        db.commit()
        db.refresh(venta)
    return venta

def eliminar_venta(db: Session, venta_id: int):
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if venta:
        db.delete(venta)
        db.commit()
        return True
    return False
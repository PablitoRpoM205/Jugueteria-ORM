from sqlalchemy.orm import Session
from entities.juguete import Juguete
from entities.inventario import Inventario
from crud.usuario_crud import obtener_usuario_por_id


def crear_juguete(
    db: Session, nombre: str, precio: float, stock: int, tipo: str, usuario_id: int
):
    nuevo_juguete = Juguete(
        nombre=nombre, precio=precio, stock=stock, tipo=tipo, usuario_id=usuario_id
    )
    db.add(nuevo_juguete)
    db.commit()
    db.refresh(nuevo_juguete)

    inventario = Inventario(
        juguete_id=nuevo_juguete.id, usuario_id=usuario_id, cantidad=stock
    )
    db.add(inventario)
    db.commit()
    db.refresh(inventario)
    return nuevo_juguete


def obtener_juguetes(db: Session):
    return db.query(Juguete).all()


def obtener_juguete_por_id(db: Session, juguete_id: int):
    return db.query(Juguete).filter(Juguete.id == juguete_id).first()


def actualizar_juguete(
    db: Session, juguete_id: int, nombre: str, precio: float, stock: int, tipo: str
):
    juguete = obtener_juguete_por_id(db, juguete_id)
    if juguete:
        juguete.nombre = nombre
        juguete.precio = precio
        juguete.stock = stock
        juguete.tipo = tipo
        db.commit()
        db.refresh(juguete)
        return juguete
    return None


def eliminar_juguete(db: Session, juguete_id: int) -> bool:
    juguete = db.query(Juguete).filter(Juguete.id == juguete_id).first()
    if not juguete:
        return False
    db.delete(juguete)
    db.commit()
    return True

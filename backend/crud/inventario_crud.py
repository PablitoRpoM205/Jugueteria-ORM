from sqlalchemy.orm import Session
from entities.inventario import Inventario
from entities.juguete import Juguete
from typing import Optional


def obtener_inventario(db: Session):
    return db.query(Inventario).all()


def actualizar_inventario(
    db: Session, inventario_id: int, inventario_data: dict
) -> Optional[Inventario]:
    inventario = db.query(Inventario).filter(Inventario.id == inventario_id).first()
    if not inventario:
        return None

    cantidad = inventario_data.get("cantidad")
    if cantidad is not None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero")
        inventario.cantidad = cantidad

    for key, value in inventario_data.items():
        if key != "cantidad" and hasattr(inventario, key):
            setattr(inventario, key, value)

    juguete = db.query(Juguete).filter(Juguete.id == inventario.juguete_id).first()
    if juguete:
        if cantidad is not None:
            juguete.stock = cantidad
        if "nombre_juguete" in inventario_data:
            juguete.nombre = inventario_data["nombre_juguete"]

    db.commit()
    db.refresh(inventario)
    return inventario


def crear_inventario(
    db: Session, usuario_id: int, juguete_id: int, cantidad: int
) -> Inventario:
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero")

    inventario_existente = (
        db.query(Inventario)
        .filter_by(usuario_id=usuario_id, juguete_id=juguete_id)
        .first()
    )

    if inventario_existente:
        inventario_existente.cantidad += cantidad
        db.commit()
        db.refresh(inventario_existente)
        return inventario_existente

    juguete = (
        db.query(Juguete).filter(Juguete.id == nuevo_inventario.juguete_id).first()
    )
    if juguete:
        juguete.stock = nuevo_inventario.cantidad

    nuevo_inventario = Inventario(
        usuario_id=usuario_id, juguete_id=juguete_id, cantidad=cantidad
    )
    db.add(nuevo_inventario)

    juguete = db.query(Juguete).filter(Juguete.id == juguete_id).first()
    if juguete:
        juguete.stock = cantidad

    db.commit()
    db.refresh(nuevo_inventario)
    return nuevo_inventario

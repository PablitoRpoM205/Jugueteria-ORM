from sqlalchemy.orm import Session
from entities.venta import Venta
from entities.juguete import Juguete
from entities.inventario import Inventario
from database.connection import SessionLocal
from typing import Optional
from fastapi import HTTPException


def crear_venta(db: Session, juguete_id: int, cantidad: int, usuario_id: int) -> Venta:
    inventario = (
        db.query(Inventario)
        .filter(
            Inventario.juguete_id == juguete_id,
            Inventario.usuario_id == usuario_id,
        )
        .first()
    )
    if not inventario:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontró inventario para el juguete {juguete_id} y usuario {usuario_id}",
        )
    if inventario.cantidad < cantidad:
        raise HTTPException(
            status_code=400,
            detail=f"Stock insuficiente: hay {inventario.cantidad}, se requieren {cantidad}",
        )

    inventario.cantidad -= cantidad

    juguete = db.query(Juguete).filter_by(id=juguete_id).first()
    if not juguete:
        raise HTTPException(
            status_code=404, detail=f"No se encontró el juguete con ID {juguete_id}"
        )
    juguete.stock = inventario.cantidad

    nueva_venta = Venta(juguete_id=juguete_id, cantidad=cantidad, usuario_id=usuario_id)
    db.add(nueva_venta)

    db.commit()
    db.refresh(nueva_venta)
    db.refresh(inventario)
    db.refresh(juguete)
    return nueva_venta


def obtener_ventas(db: Session):
    return db.query(Venta).all()


def obtener_venta_por_id(db: Session, venta_id: int) -> Optional[Venta]:
    return db.query(Venta).filter(Venta.id == venta_id).first()


def actualizar_venta(
    db: Session, venta_id: int, usuario_id: int, juguete_id: int, nueva_cantidad: int
) -> Venta:
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        return None

    inventario = (
        db.query(Inventario)
        .filter(
            Inventario.juguete_id == venta.juguete_id,
            Inventario.usuario_id == venta.usuario_id,
        )
        .first()
    )

    if not inventario:
        raise Exception("Inventario no encontrado para la venta existente")
    diferencia_cantidad = nueva_cantidad - venta.cantidad

    if diferencia_cantidad > 0:
        if inventario.cantidad < diferencia_cantidad:
            raise Exception("Inventario insuficiente para aumentar la cantidad")
        inventario.cantidad -= diferencia_cantidad
    elif diferencia_cantidad < 0:
        inventario.cantidad += abs(diferencia_cantidad)

    juguete = db.query(Juguete).filter(Juguete.id == venta.juguete_id).first()
    if juguete:
        juguete.stock = inventario.cantidad

    venta.usuario_id = usuario_id
    venta.juguete_id = juguete_id
    venta.cantidad = nueva_cantidad

    db.commit()
    db.refresh(venta)
    return venta


def eliminar_venta(db: Session, venta_id: int) -> bool:
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        return False

    inventario = (
        db.query(Inventario)
        .filter(
            Inventario.juguete_id == venta.juguete_id,
            Inventario.usuario_id == venta.usuario_id,
        )
        .first()
    )
    if inventario:
        inventario.cantidad += venta.cantidad
        juguete = db.query(Juguete).filter(Juguete.id == venta.juguete_id).first()
        if juguete:
            juguete.stock = inventario.cantidad

        db.delete(venta)
        db.commit()
        return True
    return False

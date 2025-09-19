"""
Operaciones para juguetes e inventario.
"""

from sqlalchemy.orm import Session
from entities.juguete import Juguete
from entities.inventario import Inventario
from entities.venta import Venta


def crear_juguete(
    db: Session, nombre: str, precio: float, stock: int, tipo: str, actor_id
):
    """
    Crea un juguete nuevo.
    """
    nuevo = Juguete(
        nombre=nombre,
        precio=precio,
        stock=stock,
        tipo=tipo,
        id_usuario_creacion=actor_id,
        id_usuario_edicion=actor_id,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def obtener_juguetes(db: Session):
    """
    Retorna todos los juguetes.
    """
    return db.query(Juguete).order_by(Juguete.nombre).all()


def buscar_juguete_por_nombre(db: Session, nombre: str):
    return db.query(Juguete).filter(Juguete.nombre.ilike(f"%{nombre}%")).all()


def vender_juguete(db: Session, juguete_id, usuario_id_vendio, cantidad: int):
    juguete = db.get(Juguete, juguete_id)
    if not juguete:
        return False, "Juguete no encontrado."

    if cantidad <= 0 or cantidad > juguete.stock:
        return False, "Stock insuficiente."

    precio_unitario = juguete.precio
    total = precio_unitario * cantidad
    juguete.stock -= cantidad
    venta = Venta(
        usuario_id_vendio=usuario_id_vendio,
        juguete_id=juguete.id,
        cantidad=cantidad,
        precio_unitario=precio_unitario,
        total=total,
        id_usuario_creacion=usuario_id_vendio,
        id_usuario_edicion=usuario_id_vendio,
    )
    db.add(venta)
    db.commit()
    db.refresh(venta)
    return True, venta


def aplicar_descuento(db: Session, juguete_id, porcentaje: int, actor_id=None):
    juguete = db.get(Juguete, juguete_id)
    if not juguete:
        return False, "Juguete no encontrado."

    limites = {"electronico": 20, "didactico": 15, "coleccionable": 4}
    max_desc = limites.get(juguete.tipo.lower(), 10)
    aplicado = porcentaje
    mensaje = None
    if porcentaje > max_desc:
        aplicado = max_desc
        mensaje = f"Se aplicó el máximo de {max_desc}% para tipo {juguete.tipo}."

    juguete.precio = juguete.precio * (1 - aplicado / 100)
    juguete.id_usuario_edicion = actor_id
    db.commit()
    db.refresh(juguete)
    if mensaje:
        return True, mensaje
    return True, f"Descuento aplicado: {aplicado}%. Nuevo precio: {juguete.precio:.2f}"


def eliminar_juguete(db: Session, juguete_id: int):
    """
    Elimina un juguete por su ID si no tiene ventas asociadas.
    """
    juguete = db.get(Juguete, juguete_id)
    if not juguete:
        return False, "Juguete no encontrado."
    ventas = db.query(Venta).filter(Venta.juguete_id == juguete_id).count()
    if ventas > 0:
        return (
            False,
            "No se puede eliminar: ya existen ventas asociadas a este juguete.",
        )
    db.delete(juguete)
    db.commit()
    return True, f"Juguete '{juguete.nombre}' eliminado correctamente."

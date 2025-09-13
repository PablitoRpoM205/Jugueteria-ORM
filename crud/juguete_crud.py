from sqlalchemy.orm import Session
from entities.juguete import Juguete

def crear_juguete(db: Session, nombre: str, precio: float, stock: int, tipo: str):
    nuevo_juguete = Juguete(nombre=nombre, precio=precio, stock=stock, tipo=tipo)
    db.add(nuevo_juguete)
    db.commit()
    db.refresh(nuevo_juguete)
    return nuevo_juguete

def obtener_juguetes(db: Session):
    return db.query(Juguete).all()

def obtener_juguete_por_nombre(db: Session, nombre: str):
    return db.query(Juguete).filter(Juguete.nombre.ilike(nombre)).first()

def vender_juguete(db: Session, nombre: str, cantidad: int):
    juguete = obtener_juguete_por_nombre(db, nombre)
    if not juguete:
        return "Juguete no encontrado."
    if cantidad <= 0 or cantidad > juguete.stock:
        return "No hay suficiente stock."
    juguete.stock -= cantidad
    db.commit()
    return f"Se vendieron {cantidad} {juguete.nombre}(s)."

def aplicar_descuento(db: Session, nombre: str, porcentaje: int):
    juguete = obtener_juguete_por_nombre(db, nombre)
    if not juguete:
        return "Juguete no encontrado."

    limites = {"electronico": 20, "didactico": 15, "coleccionable": 4}
    max_descuento = limites.get(juguete.tipo.lower(), 10)

    if porcentaje > max_descuento:
        porcentaje = max_descuento
        msg = f"El porcentaje máximo para {juguete.tipo} es {max_descuento}%."
    else:
        msg = f"Se aplicó el {porcentaje}% de descuento."

    juguete.precio -= juguete.precio * (porcentaje / 100)
    db.commit()
    return f"{msg} Nuevo precio: {juguete.precio:.2f}"

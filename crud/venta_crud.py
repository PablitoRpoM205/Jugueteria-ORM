"""
Consultas relacionadas con ventas.
"""

from sqlalchemy.orm import Session
from entities.venta import Venta


def listar_ventas(db: Session, limit: int = 100):
    """
    Retorna las últimas ventas.
    """
    return db.query(Venta).order_by(Venta.fecha_venta.desc()).limit(limit).all()

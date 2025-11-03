from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.venta import VentaCreate, VentaResponse
from crud.venta_crud import (
    crear_venta,
    obtener_ventas,
    obtener_venta_por_id,
    actualizar_venta,
    eliminar_venta,
)
from api.dependencias import get_db
from utils.exceptions import VentaNoEncontrada, StockInsuficiente

router = APIRouter()


@router.get("/", response_model=list[VentaResponse])
def listar_ventas(db: Session = Depends(get_db)):
    """Listar todas las ventas"""
    return obtener_ventas(db)


@router.post("/", response_model=VentaResponse, status_code=201)
def crear_venta_endpoint(venta: VentaCreate, db: Session = Depends(get_db)):
    """Crear una nueva venta"""
    try:
        nueva_venta = crear_venta(
            db, venta.juguete_id, venta.cantidad, venta.usuario_id
        )
        return nueva_venta
    except ValueError as e:
        if "stock insuficiente" in str(e).lower():
            raise StockInsuficiente()
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{venta_id}", response_model=VentaResponse)
def obtener_venta_endpoint(venta_id: int, db: Session = Depends(get_db)):
    """Obtener una venta por ID"""
    venta = obtener_venta_por_id(db, venta_id)
    if not venta:
        raise VentaNoEncontrada()
    return venta


@router.put("/{venta_id}", response_model=VentaResponse)
def actualizar_venta_endpoint(
    venta_id: int, venta: VentaCreate, db: Session = Depends(get_db)
):
    """Actualizar una venta"""
    venta_actualizada = actualizar_venta(
        db, venta_id, venta.usuario_id, venta.juguete_id, venta.cantidad
    )
    if not venta_actualizada:
        raise VentaNoEncontrada()
    return venta_actualizada


@router.delete("/{venta_id}", status_code=204)
def eliminar_venta_endpoint(venta_id: int, db: Session = Depends(get_db)):
    """Eliminar una venta"""
    eliminado = eliminar_venta(db, venta_id)
    if not eliminado:
        raise VentaNoEncontrada()
    return None

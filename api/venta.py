from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from crud.venta_crud import (
    crear_venta,
    obtener_ventas,
    obtener_venta_por_id,
    actualizar_venta,
    eliminar_venta,
)
from pydantic import BaseModel

router = APIRouter()


# Esquema Pydantic para Venta
class VentaSchema(BaseModel):
    id: int | None = None
    usuario_id: int
    juguete_id: int
    cantidad: int

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/ventas", response_model=list[VentaSchema])
def listar_ventas(db: Session = Depends(get_db)):
    return obtener_ventas(db)


@router.post("/ventas", response_model=VentaSchema)
def crear_venta_endpoint(venta: VentaSchema, db: Session = Depends(get_db)):
    nueva_venta = crear_venta(db, venta.usuario_id, venta.juguete_id, venta.cantidad)
    return nueva_venta


@router.get("/ventas/{venta_id}", response_model=VentaSchema)
def obtener_venta_endpoint(venta_id: int, db: Session = Depends(get_db)):
    venta = obtener_venta_por_id(db, venta_id)
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta


@router.put("/ventas/{venta_id}", response_model=VentaSchema)
def actualizar_venta_endpoint(
    venta_id: int, venta: VentaSchema, db: Session = Depends(get_db)
):
    venta_actualizada = actualizar_venta(db, venta_id, venta)
    if not venta_actualizada:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta_actualizada


@router.delete("/ventas/{venta_id}", response_model=dict)
def eliminar_venta_endpoint(venta_id: int, db: Session = Depends(get_db)):
    eliminado = eliminar_venta(db, venta_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return {"detail": "Venta eliminada correctamente"}

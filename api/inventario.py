from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from crud.inventario_crud import (
    obtener_inventario,
    actualizar_inventario,
)
from pydantic import BaseModel

router = APIRouter()


# Esquema Pydantic para Inventario
class InventarioSchema(BaseModel):
    id: int | None = None
    nombre: str
    cantidad: int
    juguete_id: int

    class Config:
        orm_mode = True


# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/inventario", response_model=list[InventarioSchema])
def listar_inventario(db: Session = Depends(get_db)):
    return obtener_inventario(db)


@router.put("/inventario/{inventario_id}", response_model=InventarioSchema)
def modificar_inventario(
    inventario_id: int, inventario: InventarioSchema, db: Session = Depends(get_db)
):
    actualizado = actualizar_inventario(
        db, inventario_id, inventario.dict(exclude_unset=True)
    )
    if not actualizado:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return actualizado

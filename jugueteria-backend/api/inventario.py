from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from schemas.inventario import InventarioCreate, InventarioResponse
from crud.inventario_crud import (
    obtener_inventario,
    actualizar_inventario,
    crear_inventario,
)
from entities.inventario import Inventario
from entities.juguete import Juguete
from entities.usuario import Usuario
from api.dependencias import get_db
from utils.exceptions import InventarioNoEncontrado

router = APIRouter()


@router.get("/", response_model=list[InventarioResponse])
def listar_inventario(db: Session = Depends(get_db)):
    """Listar todo el inventario"""
    inventario = db.query(Inventario).options(joinedload(Inventario.juguete)).all()
    return inventario


@router.post("/", response_model=InventarioResponse)
def crear_inventario_endpoint(
    inventario: InventarioCreate, db: Session = Depends(get_db)
):
    juguete = db.query(Juguete).filter(Juguete.id == inventario.juguete_id).first()
    if not juguete:
        raise HTTPException(
            status_code=404, detail=f"Juguete con ID {inventario.juguete_id} no existe"
        )

    usuario = db.query(Usuario).filter(Usuario.id == inventario.usuario_id).first()
    if not usuario:
        raise HTTPException(
            status_code=404, detail=f"Usuario con ID {inventario.usuario_id} no existe"
        )

    nuevo_inventario = crear_inventario(
        db,
        usuario_id=inventario.usuario_id,
        juguete_id=inventario.juguete_id,
        cantidad=inventario.cantidad,
    )
    juguete.stock = nuevo_inventario.cantidad
    db.commit()

    return nuevo_inventario


@router.put("/{inventario_id}", response_model=InventarioResponse)
def modificar_inventario(
    inventario_id: int,
    inventario: InventarioCreate,
    db: Session = Depends(get_db),
):
    """Actualizar un registro de inventario"""
    actualizado = actualizar_inventario(
        db,
        inventario_id,
        {
            "juguete_id": inventario.juguete_id,
            "cantidad": inventario.cantidad,
            "usuario_id": inventario.usuario_id,
        },
    )
    if not actualizado:
        raise InventarioNoEncontrado()
    return actualizado

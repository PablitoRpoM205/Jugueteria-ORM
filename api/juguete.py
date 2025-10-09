from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schemas.juguete import JugueteCreate, JugueteResponse
from crud.juguete_crud import (
    crear_juguete,
    obtener_juguetes,
    obtener_juguete_por_id,
    actualizar_juguete,
    eliminar_juguete,
)
from entities.juguete import Juguete
from api.dependencias import get_db
from utils.exceptions import JugueteNoEncontrado, JugueteTieneRelaciones

router = APIRouter()


@router.post("/", response_model=JugueteResponse, status_code=201)
def crear_juguete_endpoint(juguete: JugueteCreate, db: Session = Depends(get_db)):
    """Crear un nuevo juguete"""
    try:
        nuevo_juguete = crear_juguete(
            db,
            juguete.nombre,
            juguete.precio,
            juguete.stock,
            juguete.tipo,
            juguete.usuario_id,
        )
        return nuevo_juguete
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="El usuario_id proporcionado no existe."
        )


@router.get("/", response_model=list[JugueteResponse])
def obtener_juguetes_endpoint(db: Session = Depends(get_db)):
    """Listar todos los juguetes"""
    return obtener_juguetes(db)


@router.get("/{juguete_id}", response_model=JugueteResponse)
def obtener_juguete_endpoint(juguete_id: int, db: Session = Depends(get_db)):
    """Obtener un juguete por ID"""
    juguete = obtener_juguete_por_id(db, juguete_id)
    if juguete is None:
        raise JugueteNoEncontrado(juguete_id)
    return juguete


@router.put("/{juguete_id}", response_model=JugueteResponse)
def actualizar_juguete_endpoint(
    juguete_id: int, juguete: JugueteCreate, db: Session = Depends(get_db)
):
    """Actualizar un juguete"""
    actualizado = actualizar_juguete(
        db, juguete_id, juguete.nombre, juguete.precio, juguete.stock, juguete.tipo
    )
    if not actualizado:
        raise JugueteNoEncontrado(juguete_id)
    return actualizado


@router.delete("/{juguete_id}", status_code=204)
def eliminar_juguete_endpoint(juguete_id: int, db: Session = Depends(get_db)):
    """Eliminar un juguete"""
    juguete = db.query(Juguete).filter(Juguete.id == juguete_id).first()
    if not juguete:
        raise JugueteNoEncontrado(juguete_id)

    if juguete.inventario:
        raise JugueteTieneRelaciones()

    eliminado = eliminar_juguete(db, juguete_id)
    if not eliminado:
        raise JugueteNoEncontrado(juguete_id)

    return None

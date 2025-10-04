from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from crud.juguete_crud import (
    crear_juguete,
    obtener_juguetes,
    obtener_juguete_por_id,
    actualizar_juguete,
    eliminar_juguete,
)
from database.connection import SessionLocal
from entities.juguete import Juguete
from pydantic import BaseModel

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class JugueteSchema(BaseModel):
    id: int | None = None
    nombre: str
    precio: float
    stock: int
    tipo: str
    usuario_id: int

    class Config:
        orm_mode = True


@router.post("/", response_model=JugueteSchema)
def crear_juguete_endpoint(juguete: JugueteSchema, db: Session = Depends(get_db)):
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


@router.get("/", response_model=list[JugueteSchema])
def obtener_juguetes_endpoint(db: Session = Depends(get_db)):
    return obtener_juguetes(db)


@router.get("/{juguete_id}", response_model=JugueteSchema)
def obtener_juguete_endpoint(juguete_id: int, db: Session = Depends(get_db)):
    juguete = obtener_juguete_por_id(db, juguete_id)
    if juguete is None:
        raise HTTPException(status_code=404, detail="Juguete no encontrado")
    return juguete


@router.put("/{juguete_id}", response_model=JugueteSchema)
def actualizar_juguete_endpoint(
    juguete_id: int, juguete: JugueteSchema, db: Session = Depends(get_db)
):
    actualizado = actualizar_juguete(db, juguete_id, juguete.dict(exclude_unset=True))
    if not actualizado:
        raise HTTPException(status_code=404, detail="Juguete no encontrado")
    return actualizado


@router.delete("/{juguete_id}", response_model=dict)
def eliminar_juguete_endpoint(juguete_id: int, db: Session = Depends(get_db)):
    eliminado = eliminar_juguete(db, juguete_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Juguete no encontrado")
    return {"detail": "Juguete eliminado correctamente"}

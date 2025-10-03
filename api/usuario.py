from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from crud.usuario_crud import (
    crear_usuario,
    obtener_usuario,
    actualizar_usuario,
    eliminar_usuario,
    listar_usuarios,
)
from database.connection import SessionLocal
from pydantic import BaseModel

router = APIRouter()


# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UsuarioSchema(BaseModel):
    id: int | None = None
    nombre: str
    correo: str
    contrasena: str

    class Config:
        orm_mode = True


@router.post("/usuarios/", response_model=UsuarioSchema)
def crear_usuario_endpoint(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    nuevo_usuario = crear_usuario(
        db, usuario.nombre, usuario.correo, usuario.contrasena
    )
    return nuevo_usuario


@router.get("/usuarios/", response_model=list[UsuarioSchema])
def listar_usuarios_endpoint(db: Session = Depends(get_db)):
    return listar_usuarios(db)


@router.get("/usuarios/{usuario_id}", response_model=UsuarioSchema)
def obtener_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    usuario = obtener_usuario(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.put("/usuarios/{usuario_id}", response_model=UsuarioSchema)
def actualizar_usuario_endpoint(
    usuario_id: int, usuario: UsuarioSchema, db: Session = Depends(get_db)
):
    usuario_actualizado = actualizar_usuario(
        db, usuario_id, usuario.dict(exclude_unset=True)
    )
    if usuario_actualizado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_actualizado


@router.delete("/usuarios/{usuario_id}", response_model=dict)
def eliminar_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    eliminado = eliminar_usuario(db, usuario_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"detail": "Usuario eliminado"}

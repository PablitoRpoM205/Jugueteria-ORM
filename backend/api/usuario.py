from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from crud.usuario_crud import (
    crear_usuario,
    obtener_usuario,
    actualizar_usuario,
    eliminar_usuario,
    listar_usuarios,
)
from entities.usuario import Usuario
from api.dependencias import get_db
from utils.exceptions import UsuarioNoEncontrado, UsuarioTieneRelaciones

router = APIRouter()


@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_usuario_endpoint(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """Crear un nuevo usuario"""
    nuevo_usuario = crear_usuario(
        db, usuario.nombre, usuario.correo, usuario.contrasena
    )
    return nuevo_usuario


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios_endpoint(db: Session = Depends(get_db)):
    """Listar todos los usuarios"""
    return listar_usuarios(db)


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    """Obtener un usuario por ID"""
    usuario = obtener_usuario(db, usuario_id)
    if usuario is None:
        raise UsuarioNoEncontrado(usuario_id)
    return usuario


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario_endpoint(
    usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)
):
    """Actualizar un usuario"""

    cambios = usuario.dict(exclude_unset=True)
    usuario_actualizado = actualizar_usuario(db, usuario_id, cambios)
    if usuario_actualizado is None:
        raise UsuarioNoEncontrado(usuario_id)
    return usuario_actualizado


@router.delete("/{usuario_id}", status_code=204)
def eliminar_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    """Eliminar un usuario"""
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise UsuarioNoEncontrado(usuario_id)

    if usuario.juguetes:
        raise UsuarioTieneRelaciones("juguetes")

    eliminado = eliminar_usuario(db, usuario_id)
    if not eliminado:
        raise UsuarioNoEncontrado(usuario_id)

    return None

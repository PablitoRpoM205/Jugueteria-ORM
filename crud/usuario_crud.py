from sqlalchemy.orm import Session
from entities.usuario import Usuario
from schemas.usuario_schema import UsuarioCreate

def crear_usuario(db: Session, usuario: UsuarioCreate):
    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        contraseña=usuario.contraseña
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def obtener_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()

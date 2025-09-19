"""
Operaciones CRUD básicas para usuarios.
Incluye creación con hash simple de contraseña y búsqueda por correo.
"""

import hashlib
from sqlalchemy.orm import Session
from entities.usuario import Usuario


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def crear_usuario(db: Session, nombre: str, correo: str, password: str, actor_id=None):
    """
    Crea un usuario y retorna la instancia.
    """
    pwd_hash = hash_password(password)
    nuevo = Usuario(
        nombre=nombre,
        correo=correo,
        password_hash=pwd_hash,
        id_usuario_creacion=actor_id,
        id_usuario_edicion=actor_id,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def autenticar(db: Session, correo: str, password: str):
    """
    Autentica por correo y contraseña, retorna usuario si coincide.
    """
    pwd_hash = hash_password(password)
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()
    if usuario and usuario.password_hash == pwd_hash:
        return usuario
    return None


def listar_usuarios(db: Session, limit: int = 50):
    """
    Retorna lista de usuarios.
    """
    return db.query(Usuario).limit(limit).all()

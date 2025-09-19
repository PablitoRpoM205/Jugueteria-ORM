"""
Operaciones CRUD para usuarios.
"""

from sqlalchemy.orm import Session
from entities.usuario import Usuario
import uuid
import hashlib
import random


def hash_password(password: str) -> str:
    """
    Hashea una contraseña usando SHA256.
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def crear_usuario(db: Session, username: str, password: str, rol: str, actor_id=None):
    """
    Crea un nuevo usuario en la base de datos.
    """
    nuevo = Usuario(
        id=uuid.uuid4(),
        nombre=username,
        nombre_usuario=username,
        correo=f"{username}@jugueteria.com",
        contraseña_hash=hash_password(password),
        telefono=random.randint(3000000000, 3999999999),
        es_admin=(rol == "admin"),
        id_usuario_creacion=(
            actor_id if actor_id else uuid.UUID("00000000-0000-0000-0000-000000000001")
        ),
        id_usuario_edicion=(
            actor_id if actor_id else uuid.UUID("00000000-0000-0000-0000-000000000001")
        ),
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def buscar_usuario_por_username(db: Session, username: str):
    """
    Busca un usuario por su nombre de usuario.
    """
    return db.query(Usuario).filter(Usuario.nombre_usuario == username).first()


def autenticar(db: Session, username: str, password: str):
    """
    Verifica credenciales de acceso.
    """
    usuario = buscar_usuario_por_username(db, username)
    if not usuario:
        return None
    if usuario.contraseña_hash == hash_password(password):
        return usuario
    return None


def listar_usuarios(db: Session):
    """
    Devuelve todos los usuarios ordenados por nombre de usuario.
    """
    return db.query(Usuario).order_by(Usuario.username).all()

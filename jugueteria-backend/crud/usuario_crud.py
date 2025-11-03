from sqlalchemy.orm import Session
from entities.usuario import Usuario
from utils.security import hash_password


def crear_usuario(db: Session, nombre: str, correo: str, contrasena: str):
    hashed = hash_password(contrasena)
    usuario = Usuario(nombre=nombre, correo=correo, contrasena=hashed)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def obtener_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def actualizar_usuario(db: Session, usuario_id: int, cambios: dict):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return None

    if "contrasena" in cambios:
        cambios["contrasena"] = hash_password(cambios["contrasena"])

    for campo, valor in cambios.items():
        setattr(usuario, campo, valor)

    db.commit()
    db.refresh(usuario)
    return usuario


def eliminar_usuario(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario


def listar_usuarios(db: Session):
    return db.query(Usuario).all()


def crear_usuario_endpoint(db: Session, usuario_data: dict):
    return crear_usuario(
        db, usuario_data["nombre"], usuario_data["correo"], usuario_data["contrasena"]
    )


def obtener_usuario_endpoint(db: Session, usuario_id: int):
    return obtener_usuario(db, usuario_id)


def obtener_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def actualizar_usuario_endpoint(db: Session, usuario_id: int, usuario_data: dict):
    return actualizar_usuario(db, usuario_id, usuario_data)


def eliminar_usuario_endpoint(db: Session, usuario_id: int):
    return eliminar_usuario(db, usuario_id)


def buscar_usuario_por_username(db: Session, username: str):
    return db.query(Usuario).filter(Usuario.nombre == username).first()


def buscar_usuario_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()

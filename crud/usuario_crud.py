from sqlalchemy.orm import Session
from entities.usuario import Usuario


def crear_usuario(db: Session, nombre: str, correo: str, contrasena: str):
    usuario = Usuario(nombre=nombre, correo=correo, contrasena=contrasena)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def obtener_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def actualizar_usuario(db: Session, usuario_id: int, usuario_data: dict):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        for key, value in usuario_data.items():
            setattr(usuario, key, value)
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


# Endpoints que usan las funciones anteriores
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

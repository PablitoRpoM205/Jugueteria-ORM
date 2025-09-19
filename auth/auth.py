"""
Módulo de autenticación con funciones de login y registro en consola.
"""

from sqlalchemy.orm import Session
from crud.usuario_crud import crear_usuario, autenticar, listar_usuarios


def registrar_usuario_console(db: Session):
    username = input("Nombre de usuario: ").strip()
    password = input("Contraseña (mín 6 caracteres): ").strip()
    rol = input("Rol (admin/usuario): ").strip()
    if len(password) < 6:
        print("La contraseña debe tener al menos 6 caracteres.")
        return None
    user = crear_usuario(db, username, password, rol)
    print(f"Usuario creado: {user.nombre_usuario} ({user.correo})")
    return user


def login_console(db: Session):
    """
    Login por consola. Devuelve la instancia de usuario autenticado o None.
    """
    username = input("Nombre de usuario: ").strip()
    password = input("Contraseña: ").strip()
    user = autenticar(db, username, password)
    if not user:
        print("Credenciales inválidas.")
        return None
    print(f"Bienvenido {user.nombre_usuario}!")
    return user

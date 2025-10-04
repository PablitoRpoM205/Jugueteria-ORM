from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from crud.usuario_crud import crear_usuario, buscar_usuario_por_username
from sqlalchemy.orm import Session
from database.connection import SessionLocal

router = APIRouter()

class UsuarioBase(BaseModel):
    nombre: str
    correo: str
    contraseña: str

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

@router.post("/register", response_model=Usuario)
def register_usuario(usuario: UsuarioCreate):
    db: Session = SessionLocal()
    db_usuario = buscar_usuario_por_username(db, usuario.correo)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    nuevo_usuario = crear_usuario(db, usuario.nombre, usuario.correo, usuario.contraseña)
    return nuevo_usuario

@router.post("/login")
def login_usuario(usuario: UsuarioBase):
    db: Session = SessionLocal()
    db_usuario = buscar_usuario_por_username(db, usuario.correo)
    if not db_usuario or db_usuario.contraseña != usuario.contraseña:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    return {"message": "Inicio de sesión exitoso", "usuario": db_usuario.nombre}

# Aquí se pueden agregar más endpoints relacionados con la autenticación según sea necesario.
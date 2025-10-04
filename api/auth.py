from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from crud.usuario_crud import crear_usuario, buscar_usuario_por_username

router = APIRouter()

class UsuarioCreate(BaseModel):
    nombre: str
    correo: str
    contraseña: str

@router.post("/register")
async def register_usuario(usuario: UsuarioCreate):
    usuario_creado = crear_usuario(usuario.nombre, usuario.correo, usuario.contraseña)
    if not usuario_creado:
        raise HTTPException(status_code=400, detail="Error al crear el usuario")
    return {"mensaje": "Usuario creado exitosamente", "usuario_id": usuario_creado.id}

class UsuarioLogin(BaseModel):
    correo: str
    contraseña: str

@router.post("/login")
async def login_usuario(usuario: UsuarioLogin):
    usuario_encontrado = buscar_usuario_por_username(usuario.correo)
    if not usuario_encontrado or usuario_encontrado.contraseña != usuario.contraseña:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"mensaje": "Inicio de sesión exitoso", "usuario_id": usuario_encontrado.id}
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate, UsuarioLogin, UsuarioResponse
from crud.usuario_crud import crear_usuario, buscar_usuario_por_correo
from api.dependencias import get_db
from utils.security import verify_password
from utils.exceptions import CredencialesInvalidas

router = APIRouter()


@router.post("/register", response_model=UsuarioResponse, status_code=201)
async def register_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """Registrar un nuevo usuario"""
    usuario_creado = crear_usuario(
        db, usuario.nombre, usuario.correo, usuario.contrasena
    )
    return usuario_creado


@router.post("/login")
async def login_usuario(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    """Iniciar sesión"""
    usuario_encontrado = buscar_usuario_por_correo(db, usuario.correo)

    if not usuario_encontrado or not verify_password(
        usuario.contrasena, usuario_encontrado.contrasena
    ):
        raise CredencialesInvalidas()

    return {"mensaje": "Inicio de sesión exitoso", "usuario_id": usuario_encontrado.id}

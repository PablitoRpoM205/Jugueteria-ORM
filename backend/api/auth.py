from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate, UsuarioLogin, UsuarioResponse
from crud.usuario_crud import crear_usuario, buscar_usuario_por_correo
from api.dependencias import get_db
from utils.security import verify_password, create_access_token
from utils.exceptions import CredencialesInvalidas
from datetime import timedelta

router = APIRouter()


@router.post("/register", response_model=UsuarioResponse, status_code=201)
async def register_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """Registrar un nuevo usuario"""
    usuario_existente = buscar_usuario_por_correo(db, usuario.correo)
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    usuario_creado = crear_usuario(
        db, usuario.nombre, usuario.correo, usuario.contrasena, usuario.es_admin
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

    """ CREAR TOKEN JWT """
    access_token = create_access_token(
        data={
            "sub": str(usuario_encontrado.id),
            "correo": usuario_encontrado.correo,
            "nombre": usuario_encontrado.nombre,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "usuario": {
            "id": usuario_encontrado.id,
            "nombre": usuario_encontrado.nombre,
            "correo": usuario_encontrado.correo,
        },
    }

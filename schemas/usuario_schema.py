from pydantic import BaseModel, EmailStr, Field

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr

class UsuarioCreate(UsuarioBase):
    contraseña: str = Field(..., min_length=6)

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel, Field, EmailStr, validator
import re


class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    correo: EmailStr

    @validator("nombre")
    def validar_nombre(cls, v: str) -> str:
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", v):
            raise ValueError("El nombre solo puede contener letras y espacios")
        return v.strip()


class UsuarioCreate(UsuarioBase):
    contrasena: str = Field(..., min_length=8, max_length=72)

    @validator("contrasena")
    def validar_contrasena(cls, v: str) -> str:
        if not re.search(r"[A-Z]", v):
            raise ValueError("La contraseña debe contener al menos una mayúscula")
        if not re.search(r"[a-z]", v):
            raise ValueError("La contraseña debe contener al menos una minúscula")
        if not re.search(r"\d", v):
            raise ValueError("La contraseña debe contener al menos un número")
        return v


class UsuarioLogin(BaseModel):
    correo: EmailStr
    contrasena: str = Field(..., min_length=1, max_length=72)


class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        orm_mode = True


class UsuarioUpdate(BaseModel):
    nombre: str | None = Field(None, min_length=2, max_length=50)
    correo: EmailStr | None = None
    contrasena: str | None = Field(None, min_length=8, max_length=72)

    @validator("nombre")
    def validar_nombre(cls, v: str) -> str:
        if v is not None and not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", v):
            raise ValueError("El nombre solo puede contener letras y espacios")
        return v.strip() if v else v

    @validator("contrasena")
    def validar_contrasena(cls, v: str) -> str:
        if v:
            if not re.search(r"[A-Z]", v):
                raise ValueError("La contraseña debe contener al menos una mayúscula")
            if not re.search(r"[a-z]", v):
                raise ValueError("La contraseña debe contener al menos una minúscula")
            if not re.search(r"\d", v):
                raise ValueError("La contraseña debe contener al menos un número")
        return v

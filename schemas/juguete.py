from pydantic import BaseModel, Field, validator


class JugueteBase(BaseModel):
    nombre: str = Field(min_length=1, max_length=100)
    precio: float = Field(gt=0, description="El precio debe ser mayor a 0")
    stock: int = Field(ge=0, description="El stock no puede ser negativo")
    tipo: str = Field(min_length=1, max_length=50)

    @validator("nombre", "tipo")
    @classmethod
    def validar_texto(cls, v: str) -> str:
        return v.strip()


class JugueteCreate(JugueteBase):
    usuario_id: int = Field(gt=0)


class JugueteResponse(JugueteBase):
    id: int
    nombre: str
    precio: float
    stock: int
    tipo: str
    usuario_id: int

    class Config:
        orm_mode = True


class JugueteUpdate(BaseModel):
    nombre: str | None = Field(None, min_length=1, max_length=100)
    precio: float | None = Field(None, gt=0)
    stock: int | None = Field(None, ge=0)
    tipo: str | None = Field(None, min_length=1, max_length=50)

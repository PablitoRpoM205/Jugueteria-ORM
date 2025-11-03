from pydantic import BaseModel, Field
from typing import Optional


class InventarioBase(BaseModel):
    usuario_id: int = Field(gt=0)
    juguete_id: int = Field(gt=0)
    cantidad: int = Field(..., gt=0, description="Debe ser mayor que 0")


class InventarioCreate(InventarioBase):
    pass


class JugueteSimpleResponse(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True


class InventarioResponse(InventarioBase):
    id: int
    juguete_id: int
    usuario_id: int
    cantidad: int
    juguete: Optional[JugueteSimpleResponse] = None

    class Config:
        orm_mode = True

    @property
    def nombre_juguete(self) -> str:
        """Obtiene el nombre del juguete desde la relación"""
        return self.juguete.nombre if self.juguete else ""


class InventarioUpdate(BaseModel):
    nombre_juguete: str | None = None
    cantidad: int | None = Field(None, gt=0, description="Debe ser mayor que 0")

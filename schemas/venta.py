from pydantic import BaseModel, Field


class VentaBase(BaseModel):
    usuario_id: int = Field(gt=0)
    juguete_id: int = Field(gt=0)
    cantidad: int = Field(gt=0, description="La cantidad debe ser mayor a 0")


class VentaCreate(VentaBase):
    pass


class VentaResponse(VentaBase):
    id: int
    usuario_id: int
    juguete_id: int
    cantidad: int

    class Config:
        orm_mode = True


class VentaUpdate(BaseModel):
    usuario_id: int | None = Field(None, gt=0)
    juguete_id: int | None = Field(None, gt=0)
    cantidad: int | None = Field(None, gt=0)

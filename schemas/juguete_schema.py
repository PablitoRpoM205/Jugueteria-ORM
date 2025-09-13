from pydantic import BaseModel, Field

class JugueteBase(BaseModel):
    nombre: str
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    tipo: str

class JugueteCreate(JugueteBase):
    pass

class JugueteOut(JugueteBase):
    id: int

    class Config:
        orm_mode = True

from fastapi import FastAPI

app = FastAPI()

from api.usuario import router as usuario_router
from api.juguete import router as juguete_router
from api.venta import router as venta_router
from api.inventario import router as inventario_router
from api.auth import router as auth_router


app.include_router(usuario_router, prefix="/usuarios", tags=["usuarios"])
app.include_router(juguete_router, prefix="/juguetes", tags=["juguetes"])
app.include_router(venta_router, prefix="/ventas", tags=["ventas"])
app.include_router(inventario_router, prefix="/inventario", tags=["inventario"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])

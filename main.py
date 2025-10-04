from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import engine
from entities.base import Base
from api.usuario import router as usuario_router
from api.juguete import router as juguete_router
from api.venta import router as venta_router
from api.inventario import router as inventario_router
from api.auth import router as auth_router

# Crear la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(usuario_router, prefix="/usuarios", tags=["usuarios"])
app.include_router(juguete_router, prefix="/juguetes", tags=["juguetes"])
app.include_router(venta_router, prefix="/ventas", tags=["ventas"])
app.include_router(inventario_router, prefix="/inventario", tags=["inventario"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/")
def read_root():
    return {"message": "API de Juguetería funcionando"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

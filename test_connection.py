from fastapi import FastAPI
from database.connection import engine
from entities.base import Base

# Inicializar la aplicación FastAPI
app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Iniciar el servidor Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
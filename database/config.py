"""
Configuración centralizada para la base de datos.
Carga variables de entorno desde .env y expone settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")


settings = Settings()

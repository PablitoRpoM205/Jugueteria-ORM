"""
Script para probar conexión a la base de datos.
Imprime 1 si la conexión es exitosa.
"""

from sqlalchemy import text
from database.connection import engine


def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Conexión OK, resultado:", result.scalar())


if __name__ == "__main__":
    test_connection()

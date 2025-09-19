"""
Creación de engine, Session y Base para SQLAlchemy ORM.
Se usa UUID como tipo primario para PostgreSQL.
"""

import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from database.config import settings
from sqlalchemy.pool import NullPool

engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    poolclass=NullPool,
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

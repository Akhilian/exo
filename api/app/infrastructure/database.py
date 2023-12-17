import os

from sqlmodel import create_engine, SQLModel

database_path = os.getenv("DATABASE_URL", "postgresql://titanic:iceberg@localhost:5432/boat")
engine = create_engine(database_path)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

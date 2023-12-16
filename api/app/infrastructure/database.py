from sqlmodel import create_engine, SQLModel

engine = create_engine('postgresql://titanic:iceberg@localhost:5432/boat')


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

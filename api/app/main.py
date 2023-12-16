from fastapi import FastAPI, UploadFile

from adapter import import_csv
from app.infrastructure.database import create_db_and_tables
from app.infrastructure.repository import passenger_repository

app = FastAPI()


@app.post("/file")
async def ingest_csv(file: UploadFile):
    contents = await file.read()

    lines = str(contents, encoding='utf-8')
    passengers = import_csv(lines)

    passenger_repository.upsert(passengers)

    return passengers


@app.get("/passengers")
async def ingest_csv():
    return passenger_repository.get()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

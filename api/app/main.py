from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from adapter import import_csv
from app.infrastructure.database import create_db_and_tables
from app.infrastructure.repository import passenger_repository

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/file")
async def ingest_csv(file: UploadFile):
    contents = await file.read()

    lines = str(contents, encoding='utf-8')
    passengers = import_csv(lines)

    passenger_repository.upsert(passengers)

    return passengers


@app.get("/passengers", status_code=204)
async def return_passengers():
    return passenger_repository.get()


@app.get("/passengers/distribution")
async def get_distribution(axis: str):
    if axis == 'fare':
        return passenger_repository.get_price_distribution()
    return {}


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

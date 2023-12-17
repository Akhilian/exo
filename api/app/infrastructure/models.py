from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Passenger(BaseModel):
    passengerId: int = Field(default=None, primary_key=True)
    survived: int | None = None
    pclass: int | None = None
    name: str | None = None
    sex: str | None = None
    age: str | None = None
    sibSp: int | None = None
    parch: int | None = None
    ticket: str | None = None
    fare: float | None = None
    cabin: str | None = None
    embarked: str | None = None


class PassengerORM(Passenger, SQLModel, table=True):
    pass

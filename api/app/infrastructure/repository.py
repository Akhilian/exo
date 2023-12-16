from sqlmodel import Session

from app.infrastructure.database import engine
from app.models import Passenger, PassengerORM


class PassengerRepository():
    def get(self) -> list[Passenger]:
        with Session(engine) as session:
            passengers = session.query(PassengerORM).all()

            return passengers

    def upsert(passengers: list[Passenger]):
        with Session(engine) as session:
            for passenger in passengers:
                session.add(PassengerORM.from_orm(passenger))

            session.commit()


passenger_repository = PassengerRepository()

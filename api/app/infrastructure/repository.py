from sqlalchemy.orm import load_only
from sqlmodel import Session, select

from app.infrastructure.database import engine
from app.models import Passenger, PassengerORM


class PassengerRepository():
    def get(self) -> list[Passenger]:
        with Session(engine) as session:
            passengers = session.query(PassengerORM).all()

            return passengers

    def upsert(self, passengers: list[Passenger]):
        with Session(engine) as session:
            for passenger in passengers:
                session.add(PassengerORM.from_orm(passenger))

            session.commit()

    def get_price_distribution(self):
        with Session(engine) as session:
            return session.exec(
                select(
                    PassengerORM.fare,
                )
            ).all()


passenger_repository = PassengerRepository()

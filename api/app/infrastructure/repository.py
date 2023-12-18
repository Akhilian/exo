from sqlalchemy.sql.functions import count
from sqlmodel import Session, select

from app.infrastructure.database import engine
from app.infrastructure.models import Passenger, PassengerORM


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

    def get_survival_distribution(self):
        with Session(engine) as session:
            return session.query(PassengerORM.survived, count(PassengerORM.survived)).group_by(PassengerORM.survived)


passenger_repository = PassengerRepository()

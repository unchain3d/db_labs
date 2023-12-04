from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Airport(db.Model , IDto):

    __tablename__ = "Airport"

    idAirport = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_of_airport = db.Column(db.Date, nullable=True)
    score = db.Column(db.Integer, nullable=True)
    test_idtest = db.Column(db.Integer, db.ForeignKey('test.idtest'))
    clients_id = db.Column(db.Integer, db.ForeignKey('clients.id'))


    test = db.relationship("Test", backref="airports")
    clients = db.relationship("Client", backref="airports")

    def __repr__(self) -> str:
        return f"Airport(idAirport={self.idAirport}, date_of_airport={self.date_of_airport}, " \
               f"score={self.score}, test_idtest={self.test_idtest}, clients_id={self.clients_id})"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import city_controller
        from laba4.app.my_project.auth.controller import country_controller
        return {
            "idAirport": self.idAirport,
            "date_of_airport": self.date_of_airport,
            "score": self.score,
            "test_idtest": city_controller.find_by_id(self.test_idtest),
            "clients_id": country_controller.find_by_id(self.clients_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Airport:

        obj = Airport(
            date_of_airport=dto_dict.get("date_of_airport"),
            score=dto_dict.get("score"),
            test_idtest=dto_dict.get("test_idtest"),
            clients_id=dto_dict.get("clients_id"),
        )
        return obj

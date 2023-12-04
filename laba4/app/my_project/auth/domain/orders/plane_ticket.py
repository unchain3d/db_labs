from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class PlaneTicket(db.Model, IDto):

    __tablename__ = "plane_ticket"

    idplane_ticket = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flights_flights_id = db.Column(db.Integer, db.ForeignKey('flights.flights_id'), nullable=True)

    # Define relationship
    flights = db.relationship("Flight", backref="plane_ticket")

    def __repr__(self) -> str:
        return f"PlaneTicket(idplane_ticket={self.idplane_ticket}, flights_flights_id={self.flights_flights_id})"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import flight_controller
        return {
            "idplane_ticket": self.idplane_ticket,
            "flights_flights_id": flight_controller.find_by_id(self.flights_flights_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PlaneTicket:

        obj = PlaneTicket(
            idplane_ticket=dto_dict.get("idplane_ticket"),
            flights_flights_id=dto_dict.get("flights_flights_id"),
        )
        return obj

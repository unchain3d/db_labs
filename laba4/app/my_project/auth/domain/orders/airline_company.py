from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class AirlineCompany(db.Model, IDto):
    __tablename__ = "airline_company"
    idaff = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clients_id1 = db.Column(db.Integer, db.ForeignKey('clients.id'))
    flights_id1 = db.Column(db.Integer, db.ForeignKey('flights_id1.id'))

    clients = db.relationship("Course", backref="airline_companies")
    flights_id1 = db.relationship("Author", backref="airline_companies")

    def __repr__(self) -> str:
        return f"AirlineCompany(idAff={self.idaff},clients_id1={self.clients_id1}, flights_id1_id1={self.flights_id1_id1})"

    def put_into_dto(self) -> Dict[str, Any]:
        from laba4.app.my_project.auth.controller import client_history_controller
        from laba4.app.my_project.auth.controller import client_controller
        return {
            "id":self.idaff,
            "clients_id1": client_history_controller.find_by_id(self.clients_id1),
            "flights_id1_id1": client_controller.find_by_id(self.flights_id1_id1)
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AirlineCompany:
        obj = AirlineCompany(
            idaff= dto_dict.get("id"),
            clients_id1=dto_dict.get("clients_id1"),
            flights_id1_id1=dto_dict.get("flights_id1_id1"),
        )
        return obj

from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Flight(db.Model, IDto):

    __tablename__ = "flight"
    idPr = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_of_start = db.Column(db.Date, nullable=True)
    current_deadline = db.Column(db.Date, nullable=True)
    clients_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=True)
    plane_tickets_plane_tickets_id = db.Column(db.Integer, db.ForeignKey('plane_tickets.plane_tickets_id'), nullable=True)


    clients = db.relationship("Client", backref="flight")
    plane_tickets = db.relationship("PlaneTicket", backref="flight")

    def __repr__(self) -> str:
        return f"Flight(idPr={self.idPr},date_of_start={self.date_of_start}, current_deadline={self.current_deadline}, " \
               f"clients_id={self.clients_id}, plane_tickets_plane_tickets_id={self.plane_tickets_plane_tickets_id})"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import country_controller
        from laba4.app.my_project.auth.controller import plane_ticket_controller
        return {
            "id":self.idPr,
            "date_of_start": self.date_of_start,
            "current_deadline": self.current_deadline,
            "clients_id": country_controller.find_by_id(self.clients_id),
            "plane_tickets_plane_tickets_id": plane_ticket_controller.find_by_id(self.plane_tickets_plane_tickets_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Flight:

        obj = Flight(
            idPr=dto_dict.get("id"),
            date_of_start=dto_dict.get("date_of_start"),
            current_deadline=dto_dict.get("current_deadline"),
            clients_id=dto_dict.get("clients_id"),
            plane_tickets_plane_tickets_id=dto_dict.get("plane_tickets_plane_tickets_id"),
        )
        return obj

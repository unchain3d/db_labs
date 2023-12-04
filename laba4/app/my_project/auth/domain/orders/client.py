from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Client(db.Model, IDto):

    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clients_name = db.Column(db.String(45), nullable=False)
    clients_title = db.Column(db.String(45), nullable=False)
    clients_email = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.clients_name}', '{self.clients_title}', '{self.clients_email}')"

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "id": self.id,
            "clients_name": self.clients_name,
            "clients_title": self.clients_title,
            "clients_email": self.clients_email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:

        obj = Client(
            clients_name=dto_dict.get("clients_name"),
            clients_title=dto_dict.get("clients_title"),
            clients_email=dto_dict.get("clients_email"),
        )
        return obj

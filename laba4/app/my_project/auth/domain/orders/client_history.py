from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class ClientHistory(db.Model, IDto):

    __tablename__ = "client_histories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_history_name = db.Column(db.String(45), nullable=False)
    client_history_description = db.Column(db.String(300), nullable=True, default=None)
    client_history_diffc = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"ClientHistory({self.id}, '{self.client_history_name}', '{self.client_history_description}', {self.client_history_diffc})"

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "id": self.id,
            "client_history_name": self.client_history_name,
            "client_history_description": self.client_history_description,
            "client_history_diffc": self.client_history_diffc,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ClientHistory:

        obj = ClientHistory(
            client_history_name=dto_dict.get("client_history_name"),
            client_history_description=dto_dict.get("client_history_description"),
            client_history_diffc=dto_dict.get("client_history_diffc"),
        )
        return obj

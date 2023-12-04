from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class LuggageConstraints(db.Model,IDto):

    __tablename__ = "luggage_constraints"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    luggage_constraints_name = db.Column(db.String(45), nullable=False)


    def __repr__(self) -> str:
        return f"LuggageConstraints(id={self.id}, luggage_constraints_name='{self.luggage_constraints_name}', " \

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "id": self.id,
            "luggage_constraints_name": self.luggage_constraints_name,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> LuggageConstraints:

        obj = LuggageConstraints(
            luggage_constraints_name=dto_dict.get("luggage_constraints_name"),

        )
        return obj

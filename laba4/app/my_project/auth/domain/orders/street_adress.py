from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class StreetAdress(db.Model, IDto):
    __tablename__ = "street_adress"

    id_question = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_text = db.Column(db.String(200), nullable=False)
    street_adress_idstreet_adress = db.Column(db.Integer, db.ForeignKey('street_adress.idstreet_adress'))

    # Define relationship
    street_adress = db.relationship("StreetAdress", backref="street_adress_questions")

    def __repr__(self) -> str:
        return f"StreetAdressQuestion(id_question={self.id_question}, question_text='{self.question_text}', " \
               f"answers='{self.answers}', correct_answer='{self.correct_answer}', street_adress_idstreet_adress={self.street_adress_idstreet_adress})"

    def put_into_dto(self) -> Dict[str, Any]:
        from laba4.app.my_project.auth.controller import airport_controller
        return {
            "id_question": self.id_question,
            "question_text": self.question_text,
            "street_adress_idstreet_adress": airport_controller.find_by_id(self.street_adress_idstreet_adress),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> StreetAdress:
        obj = StreetAdress(
            question_text=dto_dict.get("question_text"),
            street_adress_idstreet_adress=dto_dict.get("street_adress_idstreet_adress"),
        )
        return obj

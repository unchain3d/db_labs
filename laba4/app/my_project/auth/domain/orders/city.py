from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class City(db.Model, IDto):

    __tablename__ = "City"
    idCityAns = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_answer = db.Column(db.String(200), nullable=True)
    is_correct = db.Column(db.Boolean, nullable=True)
    City_idCity= db.Column(db.Integer, db.ForeignKey('City.idCity'))
    country_id_question = db.Column(db.Integer, db.ForeignKey('country.id_country'))


    city = db.relationship("City", backref="cities")
    country = db.relationship("Country", backref="cities")

    def __repr__(self) -> str:
        return f"City(idCityAns={self.idCityAns},user_answer='{self.user_answer}', is_correct={self.is_correct}, " \
               f"City_idCity={self.City_idCity}, country_id_country={self.country_id_country})"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import city_controller
        from laba4.app.my_project.auth.controller import street_adress_controller
        return {
            "id":self.idAttemptAns,
            "user_answer": self.user_answer,
            "is_correct": self.is_correct,
            "Attempt_idAttempt": city_controller.find_by_id(self.City_idCity),
            "country_id_question": street_adress_controller.find_by_id(self.country_id_question),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> City:

        obj = City(
            idCityAns=dto_dict.get("id"),
            user_answer=dto_dict.get("user_answer"),
            is_correct=dto_dict.get("is_correct"),
            City_idCity=dto_dict.get("City_idCity"),
            country_id_question=dto_dict.get("country_id_question"),
        )
        return obj

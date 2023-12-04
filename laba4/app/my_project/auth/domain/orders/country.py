from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db


class Country(db.Model):

    __tablename__ = "countries"

    country_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_name = db.Column(db.String(45), nullable=False)
    country_position = db.Column(db.Integer, nullable=False)
    time_to_deadline = db.Column(db.Integer, nullable=True, default=None)
    cities_id = db.Column(db.Integer, db.ForeignKey('cities.id'))


    cities = db.relationship("Cities", backref="countries")

    def __repr__(self) -> str:
        return f"Country(country_id={self.country_id}, country_name='{self.country_name}', " \
               f"country_position={self.country_position}, time_to_deadline={self.time_to_deadline}, " \
               f"cities_id={self.cities_id})"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import client_history_controller
        return {
            "country_id": self.country_id,
            "country_name": self.country_name,
            "country_position": self.country_position,
            "time_to_deadline": self.time_to_deadline,
            "cities_id": client_history_controller.find_by_id(self.cities_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Country:

        obj = Country(
            country_name=dto_dict.get("country_name"),
            country_position=dto_dict.get("country_position"),
            time_to_deadline=dto_dict.get("time_to_deadline"),
            cities_id=dto_dict.get("cities_id"),
        )
        return obj

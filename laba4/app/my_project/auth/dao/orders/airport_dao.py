from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.city import Airport


class AirportDAO(GeneralDAO):
    _domain_type = Airport

from app.services.base import BaseService


class FuelService(BaseService):
    def __init__(self, fuel_repository) -> None:
        self.fuel_repository: FuelRepository = fuel_repository
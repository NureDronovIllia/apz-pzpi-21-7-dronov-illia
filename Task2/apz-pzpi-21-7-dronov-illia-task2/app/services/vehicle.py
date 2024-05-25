from app.services.base import BaseService


class VehicleService(BaseService):
    def __init__(self, vehicle_repository) -> None:
        self.vehicle_repository: VehicleRepository = vehicle_repository
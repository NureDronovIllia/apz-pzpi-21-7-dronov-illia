from app.repository.vehicle import VehicleRepository
from app.services.base import BaseService
from app.repository.inspection import InspectionRepository


class VehicleService(BaseService):
    def __init__(self, vehicle_repository, inspection_repository) -> None:
        self.vehicle_repository: VehicleRepository = vehicle_repository
        self.inspection_repository: InspectionRepository = inspection_repository

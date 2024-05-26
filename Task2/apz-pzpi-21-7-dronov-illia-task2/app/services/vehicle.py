from app.models.db.user import User
from app.models.db.vehicle import Vehicle, VehicleStatuses, VehicleTypes
from app.models.schemas.vehicle import SetStatus, VehicleBase, VehicleData, VehicleUpdate
from app.repository.inspection import InspectionRepository
from app.repository.user import UserRepository
from app.repository.vehicle import VehicleRepository
from app.services.base import BaseService


class VehicleService(BaseService):
    def __init__(
        self, user_repository, vehicle_repository, inspection_repository
    ) -> None:
        self.user_repository: UserRepository = user_repository
        self.vehicle_repository: VehicleRepository = vehicle_repository
        self.inspection_repository: InspectionRepository = inspection_repository

    async def _get_vehicles_with_status(self, vehicles: list[Vehicle]) -> list[VehicleData]:
        current_statuses: list[str] = [
            await self.vehicle_repository.get_current_status(vehicle.id)
            for vehicle in vehicles
        ]
        return [
            VehicleData(**vehicle.__dict__, current_status=VehicleStatuses(status) if status else None)
            for vehicle, status in zip(vehicles, current_statuses)
        ]

    async def get_vehicles(self, current_user: User) -> list[VehicleData]:
        await self._validate_user_permissions(self.user_repository, current_user.id)

        vehicles: list[Vehicle] = await self.vehicle_repository.get_vehicles()
        return await self._get_vehicles_with_status(vehicles)

    async def create_vehicle(
        self, data: VehicleBase, current_user: User
    ) -> VehicleData:
        await self._validate_user_permissions(self.user_repository, current_user.id)

        new_vehicle: Vehicle = await self.vehicle_repository.create_vehicle(data)
        return (await self._get_vehicles_with_status([new_vehicle]))[0]

    async def set_current_status(self, vehicle_id: int, status: SetStatus, current_user: User) -> None:
        await self._validate_user_permissions(self.user_repository, current_user.id)
        await self._validate_instance_exists(self.vehicle_repository, vehicle_id)

        await self.vehicle_repository.set_current_status(vehicle_id, status.status)

    async def update_vehicle(self, vehicle_id: int, data: VehicleUpdate, current_user: User) -> VehicleData:
        await self._validate_user_permissions(self.user_repository, current_user.id)
        await self._validate_instance_exists(self.vehicle_repository, vehicle_id)

        updated_vehicle: Vehicle = await self.vehicle_repository.update_vehicle(vehicle_id, data)
        return (await self._get_vehicles_with_status([updated_vehicle]))[0]
    
    async def delete_vehicle(self, vehicle_id: int, current_user: User) -> None:
        await self._validate_user_permissions(self.user_repository, current_user.id)
        await self._validate_instance_exists(self.vehicle_repository, vehicle_id)

        await self.vehicle_repository.delete_vehicle(vehicle_id)
        
        





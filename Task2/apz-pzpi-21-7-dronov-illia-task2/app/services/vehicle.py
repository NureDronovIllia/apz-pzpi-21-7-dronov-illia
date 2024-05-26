from app.models.db.user import User
from app.models.db.vehicle import Inspection, Vehicle, VehicleStatuses, VehicleTypes
from app.models.schemas.vehicle import (
    InspectionBase,
    InspectionData,
    InspectionUpdate,
    SetStatus,
    VehicleBase,
    VehicleData,
    VehicleUpdate,
)
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

    async def _get_vehicles_with_status(
        self, vehicles: list[Vehicle]
    ) -> list[VehicleData]:
        current_statuses: list[str] = [
            await self.vehicle_repository.get_current_status(vehicle.id)
            for vehicle in vehicles
        ]
        return [
            VehicleData(
                **vehicle.__dict__,
                current_status=VehicleStatuses(status) if status else None
            )
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

    async def set_current_status(
        self, vehicle_id: int, status: SetStatus, current_user: User
    ) -> None:
        await self._validate_user_permissions(self.user_repository, current_user.id)
        await self._validate_instance_exists(self.vehicle_repository, vehicle_id)

        await self.vehicle_repository.set_current_status(vehicle_id, status.status)

    async def update_vehicle(
        self, vehicle_id: int, data: VehicleUpdate, current_user: User
    ) -> VehicleData:
        await self._validate_user_permissions(self.user_repository, current_user.id)
        await self._validate_instance_exists(self.vehicle_repository, vehicle_id)

        updated_vehicle: Vehicle = await self.vehicle_repository.update_vehicle(
            vehicle_id, data
        )
        return (await self._get_vehicles_with_status([updated_vehicle]))[0]

    async def delete_vehicle(self, vehicle_id: int, current_user: User) -> None:
        await self._validate_user_permissions(self.user_repository, current_user.id)
        await self._validate_instance_exists(self.vehicle_repository, vehicle_id)

        await self.vehicle_repository.delete_vehicle(vehicle_id)

    async def get_inspections(self, current_user: User) -> list[VehicleData]:
        await self._validate_user_permissions(self.user_repository, current_user.id)

        inspections: list[
            Inspection
        ] = await self.inspection_repository.get_inspections()
        return [InspectionData(**inspection.__dict__) for inspection in inspections]

    async def start_inspection(
        self, data: InspectionBase, current_user: User
    ) -> InspectionData:
        await self._validate_instance_exists(self.vehicle_repository, data.vehicle_id)

        inspection: Inspection = await self.inspection_repository.create_inspection(
            data, user_id=current_user.id
        )
        return InspectionData(**inspection.__dict__)

    async def end_inspection(
        self, inspection_id: int, data: InspectionUpdate, current_user: User
    ) -> InspectionData:
        await self._validate_instance_exists(self.inspection_repository, inspection_id)

        updated_inspection: Inspection = (
            await self.inspection_repository.update_inspection(inspection_id, data)
        )
        return InspectionData(**updated_inspection.__dict__)

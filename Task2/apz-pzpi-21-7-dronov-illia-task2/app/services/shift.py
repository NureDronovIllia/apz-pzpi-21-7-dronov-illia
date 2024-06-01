from datetime import datetime

from app.models.db.shift import Shift
from app.models.db.user import User
from app.models.db.vehicle import VehicleStatuses
from app.models.schemas.shift import ShiftBase, ShiftCreate, ShiftData, ShiftUpdate
from app.repository.shift import ShiftRepository
from app.repository.user import UserRepository
from app.repository.vehicle import VehicleRepository
from app.services.base import BaseService


class ShiftService(BaseService):
    def __init__(self, user_repository, shift_repository, vehicle_repository) -> None:
        self.user_repository: UserRepository = user_repository
        self.shift_repository: ShiftRepository = shift_repository
        self.vehicle_repository: VehicleRepository = vehicle_repository

    async def get_shifts(self, current_user: User) -> list[ShiftData]:
        await self._validate_user_permissions(self.user_repository, current_user.id)

        shifts = await self.shift_repository.get_shifts()
        return [ShiftData(**shift.__dict__) for shift in shifts]

    async def start_shift(self, shift_data: ShiftBase, current_user: User) -> ShiftData:
        # Validations

        vehicle_id: int = shift_data.vehicle_id
        new_shift: Shift = await self.shift_repository.create_shift(
            ShiftCreate(vehicle_id=vehicle_id, user_id=current_user.id)
        )

        await self.vehicle_repository.set_current_status(
            vehicle_id, VehicleStatuses.SHIFT
        )

        return ShiftData(**new_shift.__dict__)

    async def end_shift(self, shift_id: int, current_user: User) -> ShiftData:
        # Validations

        shift: Shift = await self.shift_repository.get_shift(shift_id)
        # Validations

        updated_shift = await self.shift_repository.update_shift(
            shift_id, (ShiftUpdate(end_time=datetime.utcnow()))
        )
        await self.vehicle_repository.set_current_status(
            updated_shift.vehicle_id, VehicleStatuses.OFF_SHIFT
        )

        return updated_shift

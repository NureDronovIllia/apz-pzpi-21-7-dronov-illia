from fastapi import Depends
from app.repository.fuel_storage import FuelStorageRepository
from app.repository.fuel_supplier import FuelSupplierRepository
from app.repository.purchase import PurchaseRepository
from app.repository.shift import ShiftRepository
from app.repository.vehicle import VehicleRepository
from app.services.fuel import FuelService
from app.services.shift import ShiftService
from app.services.vehicle import VehicleService

from app.api.dependencies.repository import get_repository
from app.repository.user import UserRepository
from app.services.user import UserService
from app.repository.inspection import InspectionRepository


def get_user_service(
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
) -> UserService:
    service = UserService(user_repository)
    return service


def get_vehicle_service(
    vehicle_repository: VehicleRepository = Depends(get_repository(VehicleRepository)),
    inspection_repository: InspectionRepository = Depends(get_repository(InspectionRepository )),
) -> VehicleService:
    service = VehicleService(vehicle_repository, inspection_repository)
    return service


def get_shift_service(
    shift_repository: ShiftRepository = Depends(get_repository(ShiftRepository)),
) -> ShiftService:
    service = ShiftService(shift_repository)
    return service


def get_fuel_service(
    fuel_supplier_repository: FuelSupplierRepository = Depends(
        get_repository(FuelSupplierRepository)
    ),
    fuel_storage_repository: FuelStorageRepository = Depends(
        get_repository(FuelStorageRepository)
    ),
    purchase_repository: PurchaseRepository = Depends(
        get_repository(PurchaseRepository)
    ),
) -> FuelService:
    service = FuelService(
        fuel_supplier_repository, fuel_storage_repository, purchase_repository
    )
    return service

from app.repository.fuel_storage import FuelStorageRepository
from app.repository.fuel_supplier import FuelSupplierRepository
from app.repository.purchase import PurchaseRepository
from app.repository.user import UserRepository
from app.services.base import BaseService


class FuelService(BaseService):
    def __init__(
        self,
        user_repository,
        fuel_supplier_repository,
        fuel_storage_repository,
        purchase_repository,
    ) -> None:
        self.user_repository: UserRepository = user_repository
        self.fuel_supplier_repository: FuelSupplierRepository = fuel_supplier_repository
        self.fuel_storage_repository: FuelStorageRepository = fuel_storage_repository
        self.purchase_repository: PurchaseRepository = purchase_repository

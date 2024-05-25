from app.models.db.fuel import FuelSupplier
from app.repository.base import BaseRepository


class FuelSupplierRepository(BaseRepository):
    model = FuelSupplier

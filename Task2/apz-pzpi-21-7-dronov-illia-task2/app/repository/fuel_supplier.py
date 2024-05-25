from app.repository.base import BaseRepository
from app.models.db.fuel import FuelSupplier


class FuelRepository(BaseRepository):
    model = FuelSupplier
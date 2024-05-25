from app.models.db.fuel import FuelStorage
from app.repository.base import BaseRepository


class FuelStorageRepository(BaseRepository):
    model = FuelStorage

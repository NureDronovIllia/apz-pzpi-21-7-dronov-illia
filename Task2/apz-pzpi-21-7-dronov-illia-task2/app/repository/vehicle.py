from app.repository.base import BaseRepository
from app.models.db.vehicle import Vehicle


class VehicleRepository(BaseRepository):
    model = Vehicle
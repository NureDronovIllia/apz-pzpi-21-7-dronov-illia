from app.models.db.vehicle import Vehicle
from app.repository.base import BaseRepository


class VehicleRepository(BaseRepository):
    model = Vehicle

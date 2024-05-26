from app.models.db.vehicle import Inspection
from app.repository.base import BaseRepository


class InspectionRepository(BaseRepository):
    model = Inspection

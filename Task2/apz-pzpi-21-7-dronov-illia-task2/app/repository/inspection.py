from app.repository.base import BaseRepository
from app.models.db.vehicle import Inspection


class InspectionRepository(BaseRepository):
    model = Inspection
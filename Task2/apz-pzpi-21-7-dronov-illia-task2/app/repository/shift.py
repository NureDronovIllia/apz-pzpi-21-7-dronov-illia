from app.repository.base import BaseRepository
from app.models.db.shift import Shift


class ShiftRepository(BaseRepository):
    model = Shift
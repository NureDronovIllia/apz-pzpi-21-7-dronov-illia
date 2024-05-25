from app.models.db.shift import Shift
from app.repository.base import BaseRepository


class ShiftRepository(BaseRepository):
    model = Shift

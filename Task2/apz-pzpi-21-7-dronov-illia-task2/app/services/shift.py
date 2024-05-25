from app.repository.shift import ShiftRepository
from app.services.base import BaseService


class ShiftService(BaseService):
    def __init__(self, shift_repository) -> None:
        self.shift_repository: ShiftRepository = shift_repository

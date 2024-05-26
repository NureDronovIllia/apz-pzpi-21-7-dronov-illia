from app.repository.shift import ShiftRepository
from app.repository.user import UserRepository
from app.services.base import BaseService


class ShiftService(BaseService):
    def __init__(self, user_repository, shift_repository) -> None:
        self.user_repository: UserRepository = user_repository
        self.shift_repository: ShiftRepository = shift_repository

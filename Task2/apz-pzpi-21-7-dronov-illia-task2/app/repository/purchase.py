from app.models.db.fuel import Purchase
from app.repository.base import BaseRepository


class PurchaseRepository(BaseRepository):
    model = Purchase

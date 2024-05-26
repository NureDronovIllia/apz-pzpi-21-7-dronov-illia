from typing import Any, Optional

from sqlalchemy import select

from app.models.db.vehicle import Inspection
from app.repository.base import BaseRepository


class InspectionRepository(BaseRepository):
    model = Inspection

    async def get_inspections(self) -> list[Inspection]:
        query = select(Inspection)
        return self.unpack(await self.get_many(query))

    async def create_inspection(
        self, inspection_data, *args, **kwargs
    ) -> dict[str, Any]:
        new_inspection: Inspection = await self.create(inspection_data, **kwargs)
        return new_inspection

    async def update_inspection(
        self, inspection_id: int, inspection_data
    ) -> Inspection:
        updated_user = await self.update(inspection_id, inspection_data)
        return updated_user

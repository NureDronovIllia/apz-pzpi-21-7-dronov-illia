from fastapi import APIRouter, Depends

from app.api.dependencies.services import get_shift_service
from app.api.dependencies.user import get_current_user
from app.models.db.user import User
from app.services.shift import ShiftService

router = APIRouter(prefix="/shifts", tags=["Shifts"])


@router.post("/start", response_model=None, status_code=201)
async def start_shift(
    data: None,
    current_user: User = Depends(get_current_user),
    shift_service: ShiftService = Depends(get_shift_service),
) -> None:
    return await shift_service.start_shift(data, current_user)


@router.post("/{shift_id}/end/", response_model=None, status_code=201)
async def start_shift(
    shift_id: int,
    current_user: User = Depends(get_current_user),
    shift_service: ShiftService = Depends(get_shift_service),
) -> None:
    return await shift_service.end_shift(shift_id, current_user)

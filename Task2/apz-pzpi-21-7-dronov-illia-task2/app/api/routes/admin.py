from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from app.api.dependencies.services import get_user_service
from app.api.dependencies.user import get_current_user_id
from app.services.user import UserService

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/export-data/xlsx/", response_model=None)
async def export_data_xlsx(
    current_user_id: int = Depends(get_current_user_id),
    user_service: UserService = Depends(get_user_service),
):
    file_path = await user_service.export_data_xlsx(current_user_id)
    return FileResponse(
        path=file_path, filename="export.xlsx", media_type="multipart/form-data"
    )

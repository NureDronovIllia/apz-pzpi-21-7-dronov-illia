from fastapi import APIRouter

from app.api.routes.admin import router as admin_router
from app.api.routes.auth import router as auth_router

router = APIRouter()

router.include_router(router=auth_router)
router.include_router(router=admin_router)

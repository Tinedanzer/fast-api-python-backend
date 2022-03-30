from fastapi import APIRouter

from app.api.routes import admin


router = APIRouter()
router.include_router(admin.router, tags=["admin"], prefix="/admin")

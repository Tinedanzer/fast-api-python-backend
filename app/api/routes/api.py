from fastapi import APIRouter

from app.api.routes import admin, widget


router = APIRouter()
router.include_router(admin.router, tags=["admin"], prefix="/admin")
router.include_router(widget.router, tags=["widget"], prefix="/widget")

from fastapi import APIRouter

from app.api.routes import admin, widget, carebear


router = APIRouter()
router.include_router(admin.router, tags=["admin"], prefix="/admin")
router.include_router(widget.router, tags=["widget"], prefix="/widget")
router.include_router(carebear.router, tags=["carebear_info"], prefix="/carebearNation")
from fastapi import APIRouter

from app.api.routes import admin, widget, task_runner


router = APIRouter()
router.include_router(admin.router, tags=["admin"], prefix="/admin")
router.include_router(widget.router, tags=["widget"], prefix="/widget")
router.include_router(task_runner.router, tags=["task_runner"], prefix="/task-runner")

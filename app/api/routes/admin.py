from fastapi import APIRouter

from app.models.admin import (
    Ready,
    Health,
)


router = APIRouter()


@router.get(
    "/ready",
)
def is_ready() -> Ready:
    return Ready()


@router.get(
    "/health",
)
def is_healthy() -> Health:
    return Health()

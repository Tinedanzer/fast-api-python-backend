from datetime import datetime
from fastapi import APIRouter

from app.models.widgets import (
    Widget,
)


router = APIRouter()


@router.get(
    "/widget",
)
def get_widget() -> Widget:
    return Widget()

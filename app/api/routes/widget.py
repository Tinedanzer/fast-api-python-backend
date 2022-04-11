from fastapi import APIRouter

from app.models.widgets import (
    Widget,
)


router = APIRouter()


@router.get(
    "",
)
def get_widget() -> Widget:
    return Widget()

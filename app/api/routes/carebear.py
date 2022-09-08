from fastapi import APIRouter
from app.models.carebear import (
    Carebear,
)
from app.services.APIendpoint import (
    carebear_output,
)
from app.services.db_setup import *

router = APIRouter()

@router.get(
    "/carebear",
)
def is_carebear() -> Carebear():
    return Carebear()

@router.post(
    "/carebearAPI"
)
def carebear_response():
    return carebear_output
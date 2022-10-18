from fastapi import APIRouter
from app.models.carebear import (
    Carebear,
)
from app.services.APIendpoint import (
    carebear_output,
)
from app.services.db_setup import *
# from app.db.migrations.env import(
#     Travelers,
# )

router = APIRouter()

@router.get(
    "/carebear",
)
def is_carebear() -> Carebear():
    return Carebear()

@router.get(
    "/carebearAPI"
)
def carebear_response():
    return carebear_output

# @router.post(
#     "/travelerPost"
# )
# def traveler_post():
#     return Travelers
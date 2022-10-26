from fastapi import APIRouter
from app.models.carebear import (
    Carebear,
)
from app.services.APIendpoint import (
    carebear_output,
)
# from app.services.db_setup import *
from app.services.db_connection import(
    get_travelers,
)

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

@router.get(
    "/travelerPost"
)
def traveler_post():
    return get_travelers()
    # value = Return()
    # for item in value:
    #     thing = item
    # return thing
    # return Return()
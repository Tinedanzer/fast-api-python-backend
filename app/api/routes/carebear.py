from fastapi import APIRouter
from app.models.carebear import (
    Carebear,
)
from app.services.APIendpoint import (
    travelers_output,
)
# from app.services.db_setup import *
from app.services.db_connection import(
    get_travelers,
)
from app.services.db_inserts import table_insertion

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
    table_insertion('Travelers', travelers_output)
    return travelers_output

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
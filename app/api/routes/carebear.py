from fastapi import APIRouter
from app.models.carebear import (
    Carebear,
)
from app.services.APIendpoint import (
    final_traveler_output,
)
# from app.services.db_setup import *
from app.services.db_get_Travelers import(
    get_travelers,
)
from app.services.db_inserts import table_insertion
from app.services.db_removal import del_traveler

# from app.services.db_removal import 

router = APIRouter()

@router.get(
    "/carebear",
)
def is_probably_not_carebear() -> Carebear():
    return Carebear()

@router.get(
    "/Traveler_Insert_API_intoDB"
)
def traveler_insertion():
    table_insertion('Travelers', final_traveler_output)
    return final_traveler_output

@router.get(
    "/GetTravelerInfo"
)
def traveler_retrieve_all_from_db():
    return get_travelers()
    # value = Return()
    # for item in value:
    #     thing = item
    # return thing
    # return Return()

@router.post(
    '/GetWrekt'
)
def this_is_what_happens():
    del_traveler('Travelers')
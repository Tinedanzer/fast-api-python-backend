from pydantic import BaseModel
from app.services.APIendpoint import (
    final_traveler_output,
)


class Carebear(BaseModel):
    # APIresponse: repurpose
    widget_id: int = 1
    whizz: str = "hah, is carebear, is grumpy bear".upper()
    more: str = 'Dont let AK know i\'m still putting carebear stuff in here'
    bang: int = 5
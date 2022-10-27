from pydantic import BaseModel
from app.services.APIendpoint import (
    final_traveler_output,
)


class Carebear(BaseModel):
    # APIresponse: repurpose
    widget_id: int = 1
    whizz: str = "aroo"
    bang: int = 5
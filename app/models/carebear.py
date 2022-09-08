from pydantic import BaseModel
from app.services.APIendpoint import (
    repurpose,
)


class Carebear(BaseModel):
    # APIresponse: repurpose
    widget_id: int = 1
    whizz: str = "aroo"
    bang: int = 5
from datetime import datetime
from pydantic import BaseModel


class Widget(BaseModel):
    widget_id: int = 1
    whizz: str = "whoosh"
    bang: int = 5
    created_datetime: datetime = datetime.utcnow()
    updated_datetime: datetime = datetime.utcnow()

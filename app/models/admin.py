from pydantic import BaseModel


class Ready(BaseModel):
    status: str = "ready"


class Health(BaseModel):
    status: str = "healthy"

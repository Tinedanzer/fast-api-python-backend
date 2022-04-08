from pydantic import BaseModel


class Error(BaseModel):
    error: dict

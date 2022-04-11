from pydantic import BaseModel


class TaskRunner(BaseModel):
    task_id: str


class DummyFunc(BaseModel):
    arg_1: str
    arg_2: int

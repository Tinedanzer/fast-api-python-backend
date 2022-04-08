from pydantic import BaseModel


class TaskRunner(BaseModel):
    task_id: str

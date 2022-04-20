from pydantic import BaseModel


class TaskRunner(BaseModel):
    task_id: str


class DummyFunc(BaseModel):
    arg_1: str
    arg_2: int

    def __repr__(self) -> str:
        return f"arg_1=<redacted> arg_2={self.arg_2}"

    def __str__(self) -> str:
        return f"arg_1=<redacted> arg_2={self.arg_2}"

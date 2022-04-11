from fastapi import APIRouter

from app.models.task_runner import TaskRunner, DummyFunc
from app.services.celery.tasks import schedule_dummy_func


router = APIRouter()


@router.post(
    "/dummy-func",
)
def run_dummy_func_task(dummy: DummyFunc) -> TaskRunner:
    return TaskRunner(task_id=schedule_dummy_func(dummy))

from typing import Union
from celery import signature
from fastapi import APIRouter
from loguru import logger
from traceback import print_exc

from app.models.task_runner import TaskRunner
from app.models.error import Error
from app.services.celery.tasks import dummy_func


router = APIRouter()


@router.post(
    "/",
)
def run_task() -> Union[Error, TaskRunner]:
    try:
        sig = signature(dummy_func.name, args=("hello", 5))
        task = sig.apply_async()
    except Exception as e:
        logger.exception("stuff broke yo")
        print_exc()
        return Error(error=dict(type=e.__class__.__name__, args=str(e.args)))
    return TaskRunner(task_id=task.id)

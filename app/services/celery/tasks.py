from celery import signature
from loguru import logger
from app.resources.celery import cel_app
from app.models.task_runner import DummyFunc


@cel_app.task(
    time_limit=10,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 2},
    argsrepr="(arg_1, arg_2)",
)
def dummy_func(arg_1: str, arg_2: int) -> None:
    logger.info(arg_1)
    logger.info(arg_2)
    print(arg_1, arg_2)


def schedule_dummy_func(dummy: DummyFunc) -> str:
    # generate the celery signature to be called asynchronously
    sig = signature(
        dummy_func.name,
        args=(dummy.arg_1, dummy.arg_2),
    )
    logger.info(f"scheduling dummy_func task with args: {dummy}")
    # send the signature to the celery workers
    task = sig.apply_async()
    # return the task id
    return task.id

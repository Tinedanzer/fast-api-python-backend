from celery import signature
import logging
from app.resources.celery import cel_app
from app.models.task_runner import DummyFunc


logger = logging.getLogger(__name__)


@cel_app.task(
    time_limit=10,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 2},
    argsrepr="(arg_1, arg_2)",
)
def dummy_func(arg_1: str, arg_2: int) -> None:
    """
    Example function with the celery task decorator

    Args:
        arg_1 (str): first argument that is a string
        arg_2 (int): second argument that is an int

    Returns:
        None
    """
    # obj = MyFirstObject()
    # obj.execute()
    logger.info(arg_1)
    logger.info(arg_2)
    print(arg_1, arg_2)


def schedule_dummy_func(dummy: DummyFunc) -> str:
    """
    Function to schedule the dummy_func task. Will be worked by the
    next available celery worker.

    Args:
        dummy (DummyFunc): model for the payload to be applied to the function

    Returns:
        str: the task ID associated with the scheduled task
    """

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

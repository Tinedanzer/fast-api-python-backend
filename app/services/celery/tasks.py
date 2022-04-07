from app.resources.celery import cel_app


@cel_app.task(
    time_limit=900,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 2},
    argsrepr="(arg_1, arg_2)",
)
def dummy_func(arg_1: str, arg_2: int) -> None:
    print(arg_1)
    print(arg_2)
    pass

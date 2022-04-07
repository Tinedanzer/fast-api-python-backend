from celery import Celery
from os import getenv


DEFAULT_QUEUE = "default"
DEFAULT_QUEUE = "subtasks"
DATABASE_QUEUE = "database"


cel_app = Celery(
    "tasks",
    backend=getenv("CELERY_BACKEND"),
    broker=getenv("CELERY_BROKER"),
)

cel_app.autodiscover_tasks(
    [
        "app.services.celery.tasks",
    ]
)
cel_app.conf.task_default_queue = DEFAULT_QUEUE
cel_app.conf.task_routes = {
    "app.services.celery.database.*": {"queue": DATABASE_QUEUE},
    "app.services.celery.subtask.*": {"queue": DEFAULT_QUEUE},
}
cel_app.conf.broker_transport_options = {"visibility_timeout": 120}

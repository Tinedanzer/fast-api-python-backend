from celery import Celery
from os import getenv


DEFAULT_QUEUE = "default"
SUBTASKS_QUEUE = "subtasks"
DATABASE_QUEUE = "database"


class CeleryConfig:
    enable_utc = True
    broker_url = getenv("CELERY_BROKER_URL")
    result_backend = getenv("CELERY_RESULT_BACKEND")
    imports = ("app.services.celery.tasks",)
    task_annotations = {}
    worker_prefetch_multiplier = 1
    acks_late = True
    task_default_queue = DEFAULT_QUEUE
    task_routes = {
        "app.services.celery.database.*": {"queue": DATABASE_QUEUE},
        "app.services.celery.subtasks.*": {"queue": SUBTASKS_QUEUE},
    }
    broker_transport_options = {"visibility_timeout": 120}

cel_app = Celery()

cel_app.config_from_object(CeleryConfig)

cel_app.autodiscover_tasks(
    [
        "app.services.celery.tasks",
    ]
)

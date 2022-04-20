import celery
import logging
from celery.signals import after_setup_task_logger
from celery.app.log import TaskFormatter
from os import getenv


logger = logging.getLogger(__name__)


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
    worker_redirect_stdouts = False


cel_app = celery.Celery()


@after_setup_task_logger.connect
def setup_task_logger(logger, *args, **kwargs):
    for handler in logger.handlers:
        handler.setFormatter(TaskFormatter('%(asctime)s - %(task_id)s - %(task_name)s - %(name)s - %(levelname)s - %(message)s'))


cel_app.config_from_object(CeleryConfig)
setup_task_logger(logger=logger)
logger.info("blergh")


@celery.signals.setup_logging.connect
def on_setup_logging(**kwargs):
    pass


cel_app.autodiscover_tasks(
    [
        "app.services.celery.tasks",
    ]
)

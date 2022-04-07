from os import getenv


# Broker
broker_url = getenv("CELERY_BROKER")

# Backend
result_backend = getenv("CELERY_BACKEND")

# Modules to import when the Celery worker starts
imports = ("app.services.celery.tasks",)

task_annotations = {}

# Prevents a worker from grabbing all tasks
worker_prefetch_multiplier = 1

# Retry when worker fails
acks_late = True

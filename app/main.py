from fastapi import FastAPI

from app.api.routes import api
from app.resources.logging import logger


API_V1 = "/api/v1"


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(api.router, prefix=API_V1)

    return application


logger.info("setting up api...")
fast_app = get_application()

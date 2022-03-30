from fastapi import FastAPI

from app.api.routes import api


API_V1 = "/api/v1"


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(api.router, prefix=API_V1)

    return application


fast_app = get_application()

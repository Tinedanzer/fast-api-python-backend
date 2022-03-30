from fastapi import FastAPI

from app.api.routes import api

# from fastapi.exceptions import RequestValidationError
# from starlette.exceptions import HTTPException
# from starlette.middleware.cors import CORSMiddleware

# from app.api.errors.http_error import http_error_handler
# from app.api.errors.validation_error import http422_error_handler
# from app.api.routes.api import router as api_router
# from app.core.config import get_app_settings
# from app.core.events import create_start_app_handler, create_stop_app_handler


API_V1 = "/api/v1"


def get_application() -> FastAPI:
    # settings = get_app_settings()

    # settings.configure_logging()

    # application = FastAPI(**settings.fastapi_kwargs)
    application = FastAPI()

    # application.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=settings.allowed_hosts,
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )

    # application.add_event_handler(
    #     "startup",
    #     create_start_app_handler(application, settings),
    # )
    # application.add_event_handler(
    #     "shutdown",
    #     create_stop_app_handler(application),
    # )

    # application.add_exception_handler(HTTPException, http_error_handler)
    # application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api.router, prefix=API_V1)

    return application


fast_app = get_application()

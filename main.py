# from typing import List
# from fastapi.responses import HTMLResponse
# from sqlalchemy.orm import Session
#
# from api.user.schemas import UserSchema
# from library.socket_service import html_template

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi
from starlette import exceptions
from starlette.middleware.cors import CORSMiddleware

from api.routers import api_router
from library.constant.setting import (
    ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
)
from library.database import Base, engine
from library.exception import http422_error_handler, http_error_handler

Base.metadata.create_all(bind=engine)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=PROJECT_NAME + " documentation",
        version=VERSION,
        description="",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


def get_application() -> FastAPI:

    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.openapi = custom_openapi

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(exceptions.HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = get_application()

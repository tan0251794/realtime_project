from typing import Union

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def http422_error_handler(
    _: Request,
    exc: Union[RequestValidationError, ValidationError],
) -> JSONResponse:
    # NOTE: using ujson for better time dumps json
    return JSONResponse(
        {"errors": exc.errors()},
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    if isinstance(exc.detail, dict):
        content = {
            'error_code': exc.detail['error_code'],
            'description': exc.detail['description']
        }
    else:
        content = {
            'error_code': None,
            'description': exc.detail
        }

    return JSONResponse(
        content=content,
        status_code=exc.status_code
    )

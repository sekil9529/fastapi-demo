# coding: utf-8

"""请求校验异常捕获"""

from typing import Type
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from .base import BaseHandler
from ext.error_code import ECEnum
from ext.response import response_fail


class RequestValidationExecHandler(BaseHandler):
    """请求校验异常处理"""

    def get_exception(self) -> Type[Exception]:
        return RequestValidationError

    async def exc_handler(self, request, exc: RequestValidationError) -> JSONResponse:
        return response_fail(enum=ECEnum.InvalidParam, desc=exc.errors())

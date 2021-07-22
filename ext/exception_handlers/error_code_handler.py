# coding: utf-8

"""错误码异常捕获"""

from typing import Type
from starlette.responses import JSONResponse

from .base import BaseHandler
from libs.error_code.exception import ECException
from ext.response import response_fail


class ErrorCodeExecHandler(BaseHandler):
    """错误码异常处理"""

    def get_exception(self) -> Type[Exception]:
        return ECException

    async def exc_handler(self, request, exc: ECException) -> JSONResponse:
        return response_fail(enum=exc.enum)

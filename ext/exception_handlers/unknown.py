# coding: utf-8

"""未知异常捕获"""

from typing import Type
from loguru import logger
from starlette.responses import JSONResponse

from .base import BaseHandler
from ext.response import response_fail


class UnknownExecHandler(BaseHandler):
    """未知异常捕获"""

    def get_exception(self) -> Type[Exception]:
        return Exception

    async def exc_handler(self, request, exc: Exception) -> JSONResponse:
        logger.exception(exc)
        return response_fail()

# coding: utf-8

"""全局异常捕获"""

from loguru import logger
from starlette.responses import JSONResponse

from .base import BaseHandler


class GlobalHandler(BaseHandler):

    def get_exception(self) -> Exception:
        return Exception

    async def exc_handler(self, request, exc: Exception) -> JSONResponse:
        logger.exception(exc)
        return JSONResponse({'message': '服务异常'}, status_code=500)

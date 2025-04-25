"""请求校验异常捕获"""

from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from .base import BaseHandler
from core.error_code import ECEnum
from core.response import response_fail


class RequestValidationExecHandler(BaseHandler):
    """请求校验异常处理"""

    def get_exception(self) -> type[Exception]:
        return RequestValidationError

    async def exc_handler(self, request, exc: RequestValidationError) -> JSONResponse:
        return response_fail(enum=ECEnum.InvalidParam, desc=exc.errors())

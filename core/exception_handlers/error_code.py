"""错误码异常捕获"""

from starlette.responses import JSONResponse

from .base import BaseHandler
from core.error_code import ECException
from core.response import response_fail


class ErrorCodeExecHandler(BaseHandler):
    """错误码异常处理"""

    def get_exception(self) -> type[Exception]:
        return ECException

    async def exc_handler(self, request, exc: ECException) -> JSONResponse:
        return response_fail(enum=exc.enum)

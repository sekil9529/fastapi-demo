"""未知异常捕获"""

from starlette.responses import JSONResponse

from .base import BaseHandler
from core.response import response_fail
from libs.logger import LoggerProxy

logger: LoggerProxy = LoggerProxy(__name__)


class UnknownExecHandler(BaseHandler):
    """未知异常捕获"""

    def get_exception(self) -> type[Exception]:
        return Exception

    async def exc_handler(self, request, exc: Exception) -> JSONResponse:
        logger.error("unknown error", exc_info=exc)
        return response_fail()

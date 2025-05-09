"""错误码异常捕获"""

import typing as t

from exception_handler.base import BaseHandler
from helper.error_code import ECException
from helper.response import response_fail

if t.TYPE_CHECKING:
    from fastapi import Request, Response


class ErrorCodeExecHandler(BaseHandler):
    """错误码异常处理"""

    def get_exception(self) -> type["ECException"]:

        return ECException

    async def exc_handler(self, request: "Request", exc: "ECException") -> "Response":

        return response_fail(enum=exc.enum, message=exc.message)

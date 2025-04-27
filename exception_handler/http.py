# coding: utf-8

import typing as t

from starlette.exceptions import HTTPException

from exception_handler.base import BaseHandler
from helper.error_code import ECEnum
from helper.response import response_fail

if t.TYPE_CHECKING:  # pragma: no cover
    from fastapi.requests import Request
    from fastapi.responses import Response


class HTTPExceptionHandler(BaseHandler):
    """HTTP异常处理"""

    def get_exception(self) -> t.Type["HTTPException"]:

        return HTTPException

    async def exc_handler(self, request: "Request", exc: "HTTPException") -> "Response":

        return response_fail(enum=ECEnum.ClientError, desc=exc.detail)

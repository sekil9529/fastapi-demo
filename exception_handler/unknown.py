# coding: utf-8

"""未知异常捕获"""

import typing as t

from exception_handler.base import BaseHandler
from helper.response import response_fail

if t.TYPE_CHECKING:
    from fastapi import Request, Response


class UnknownExecHandler(BaseHandler):
    """未知异常捕获"""

    def get_exception(self) -> type["Exception"]:

        return Exception

    async def exc_handler(self, request: "Request", exc: "Exception") -> "Response":

        self._logger.error("unknown error", exc_info=exc)
        return response_fail()

# coding: utf-8

"""请求校验异常捕获"""

import typing as t

from fastapi.exceptions import RequestValidationError

from exception_handler.base import BaseHandler
from helper.error_code import ECEnum
from helper.response import response_fail
from util.seri import json_dumps

if t.TYPE_CHECKING:
    from fastapi import Request, Response


class RequestValidationExecHandler(BaseHandler):
    """请求校验异常处理"""

    def get_exception(self) -> type["RequestValidationError"]:

        return RequestValidationError

    async def exc_handler(self, request: "Request", exc: "RequestValidationError") -> "Response":

        desc = json_dumps(exc.errors(), return_bytes=False)
        return response_fail(enum=ECEnum.InvalidParam, desc=desc)

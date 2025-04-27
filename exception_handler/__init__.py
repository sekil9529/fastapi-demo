# coding: utf-8

"""异常捕获"""

import typing as t

from exception_handler.unknown import UnknownExecHandler
from exception_handler.http import HTTPExceptionHandler
from exception_handler.request_validation import RequestValidationExecHandler
from exception_handler.error_code import ErrorCodeExecHandler

if t.TYPE_CHECKING:
    from exception_handler.base import BaseHandler


# 异常捕获类
EXCEPTION_HANDLERS: list[type["BaseHandler"]] = [
    RequestValidationExecHandler,
    ErrorCodeExecHandler,
    HTTPExceptionHandler,
    UnknownExecHandler,
]

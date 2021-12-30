from .base import BaseHandler
from .unknown import UnknownExecHandler
from .request_validation import RequestValidationExecHandler
from .error_code import ErrorCodeExecHandler

# 异常捕获类
EXCEPTION_HANDLERS: list[type[BaseHandler]] = [
    RequestValidationExecHandler,
    ErrorCodeExecHandler,
    UnknownExecHandler,
]

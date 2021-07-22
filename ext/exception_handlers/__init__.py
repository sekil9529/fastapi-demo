# coding: utf-8

from .unknown import UnknownExecHandler
from .request_validation import RequestValidationExecHandler
from .error_code import ErrorCodeExecHandler


EXC_HDL_TUPLE = (
    UnknownExecHandler,
    RequestValidationExecHandler,
    ErrorCodeExecHandler,
)

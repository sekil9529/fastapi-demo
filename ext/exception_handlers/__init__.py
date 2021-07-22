# coding: utf-8

from .global_handler import GlobalExecHandler
from .request_validation_handler import RequestValidationExecHandler
from .error_code_handler import ErrorCodeExecHandler


EXC_HDL_TUPLE = (
    GlobalExecHandler,
    RequestValidationExecHandler,
    ErrorCodeExecHandler,
)

# coding: utf-8

from .global_exc import GlobalExecHandler
from .request_validation_exc import RequestValidationExecHandler
from .error_code_exc import ErrorCodeExecHandler


EXC_HDL_TUPLE = (
    GlobalExecHandler,
    RequestValidationExecHandler,
    ErrorCodeExecHandler,
)

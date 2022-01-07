from fastapi.responses import JSONResponse

from core.error_code import ECEnum
from core.response import response_ok
from core.error_code import ECException


async def test_error_code() -> JSONResponse:
    """测试错误码"""
    raise ECException(ECEnum.ServerError)
    return response_ok()

# coding: utf-8

import typing as t

from helper.error_code import ECEnum, ECException

if t.TYPE_CHECKING:
    from fastapi.responses import Response


async def test_error_code() -> "Response":
    """测试错误码"""

    raise ECException(ECEnum.ServerError, message="异常测试")

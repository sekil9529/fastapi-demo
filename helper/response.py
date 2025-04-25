"""响应相关"""

import typing as t
from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass as pyd_dataclass
from fastapi.responses import JSONResponse

from helper.error_code import ECEnum
from util.seri import json_dumps
from util.type import DataclassProtocol
from util.datetime import to_unix_timestamp

__all__ = (
    "response_ok",
    "response_fail",
    "ResData",
)


# 响应数据类型
_DataType = DataclassProtocol | BaseModel | dict


@pyd_dataclass
class ResData:
    """响应数据"""

    code: str = Field("0", description="错误码")
    message: str = Field("ok", description="错误信息")
    desc: str = Field("", description="错误详情")
    data: _DataType = Field(default_factory=dict, description="数据")


_RES_OK_BYTES: bytes = json_dumps(ResData(), return_bytes=True)


def response_ok(data: _DataType | None = None, /) -> JSONResponse:
    """成功返回"""

    if data is None:
        return JSONResponse(_RES_OK_BYTES)
    res = ResData(data=data)
    res_bytes = json_dumps(res, default=_default, return_bytes=True)
    return JSONResponse(res_bytes)


def response_fail(
        enum: ECEnum | None = None,
        desc: str = "") -> JSONResponse:
    """失败返回"""

    if enum is None:
        enum = ECEnum.ServerError

    res = ResData(
        code=enum.code,
        message=enum.message,
        desc=desc)
    res_bytes = json_dumps(res, default=_default, return_bytes=True)
    return JSONResponse(res_bytes)


def _default(o: t.Any) -> t.Any:

    if isinstance(o, datetime):
        return to_unix_timestamp(o)
    if isinstance(o, Decimal):
        return str(o)
    if isinstance(o, BaseModel):
        return o.model_dump_json()
    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")  # pragma: no cover

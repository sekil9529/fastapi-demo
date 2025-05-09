"""响应相关"""

import typing as t
from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, Field, create_model
from pydantic.dataclasses import dataclass as pyd_dataclass

from extra.fastapi.response import JSONResponse
from helper.error_code import ECEnum
from util.seri import json_dumps
from util.type import DataclassProtocol
from util.datetime import to_unix_timestamp

__all__ = (
    "response_ok",
    "response_fail",
    "ResData",
    "res_model_factory",
)


# 响应数据类型
_DataType = DataclassProtocol | BaseModel
# 响应模型缓存
_RES_MODEL_CACHE: dict[int, type[_DataType]] = dict()


@pyd_dataclass
class ResData:
    """响应数据"""

    code: str = Field("0", description="错误码")
    message: str = Field("ok", description="错误信息")
    desc: str = Field("", description="错误详情")
    data: t.Any = Field(default_factory=dict, description="数据")


class _ResModel(BaseModel):
    """响应模型

    仅用于文档生成
    """

    code: str = Field("0", description="错误码")
    message: str = Field("ok", description="错误信息")
    desc: str = Field("", description="错误详情")
    data: t.Any = Field(default_factory=dict, description="数据")


def res_model_factory(model: type[_DataType]) -> type[_DataType]:
    """响应模型工厂"""

    model_id: int = id(model)
    global _RES_MODEL_CACHE
    if model_id not in _RES_MODEL_CACHE:
        new_model = create_model(
            f"_{model.__name__}__{model_id}__ResModel",
            __base__=_ResModel,
            data=(model, ...)  # ... 表示必填字段
        )
        _RES_MODEL_CACHE[model_id] = new_model
    return _RES_MODEL_CACHE[model_id]


_RES_OK_BYTES: bytes = json_dumps(ResData(), return_bytes=True)


def response_ok(data: _DataType | dict | None = None, /) -> "JSONResponse":
    """成功返回"""

    if data is None:
        return JSONResponse(_RES_OK_BYTES)
    res = ResData(data=data)
    res_bytes = json_dumps(res, default=_default, return_bytes=True)
    return JSONResponse(res_bytes)


def response_fail(
        enum: ECEnum | None = None,
        message: str | None = None,
        desc: str = "") -> "JSONResponse":
    """失败返回"""

    if enum is None:
        enum = ECEnum.ServerError

    res = ResData(
        code=enum.code,
        message=message or enum.message,
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

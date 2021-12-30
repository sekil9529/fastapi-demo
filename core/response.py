"""响应相关"""

from typing import Any, Optional
import json
from decimal import Decimal
from json import JSONEncoder
from datetime import datetime

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from pydantic import BaseModel, Field

from .error_code import ECEnum
from libs.datetime import to_unix_timestamp

__all__ = (
    "ExtJsonResponse",
    "ResponseModel",
    "response_ok",
    "response_fail",
)


class _ExtJsonEncoder(JSONEncoder):
    """扩展json编码器"""
    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            return to_unix_timestamp(o)
        elif isinstance(o, Decimal):
            return str(o)
        # return super().default(o)
        return jsonable_encoder(o)


class ExtJsonResponse(JSONResponse):
    """扩展JsonResponse"""

    def render(self, content: Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            cls=_ExtJsonEncoder,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")


class ResponseModel(BaseModel):
    """响应模型"""

    code: str = Field("0", title="错误码")
    error: str = Field("", title="error码")
    message: str = Field("ok", title="信息")
    desc: str = Field("", title="详情")
    data: dict = Field(default_factory=dict, title="数据")


def response_ok(data: Optional[dict] = None, **kwargs) -> JSONResponse:
    """成功返回

    :param data: 数据
    :return:
    """
    if data is None:
        data = {}
    data.update(kwargs)
    content: dict[str, Any] = ResponseModel(data=data).dict()
    return ExtJsonResponse(content, status_code=status.HTTP_200_OK)


def response_fail(
        enum: Optional[ECEnum] = None,
        desc: Any = "") -> JSONResponse:
    """失败返回

    :param enum: 错误码枚举类
    :param desc: 错误详情
    :return:
    """
    if enum is None:
        enum = ECEnum.ServerError
    # 错误码
    code: str = str(enum.code)
    # error码
    error: str = enum.error
    # 错误信息
    message: str = enum.message
    # 内容
    content: dict[str, Any] = ResponseModel(code=code, error=error, message=message, desc=desc).dict()
    # 响应状态码
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR if code == "500" else status.HTTP_200_OK
    return ExtJsonResponse(content, status_code=status_code)

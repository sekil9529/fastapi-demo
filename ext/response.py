# coding: utf-8

"""响应相关配置"""

from typing import Any, Dict, Optional
import json
from decimal import Decimal
from json import JSONEncoder
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status

from .error_code import ECEnum
from libs.error_code.exception import ECException
from libs.datetime import to_unix_timestamp


class ExtJsonEncoder(JSONEncoder):
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
            cls=ExtJsonEncoder,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")


def response_ok(data: Any) -> JSONResponse:
    """成功返回

    :param data: 数据
    :return:
    """
    # 错误码
    code: str = '0'
    # 内容
    content: Dict[str, Any] = dict(code=code, data=data)
    return ExtJsonResponse(content, status_code=status.HTTP_200_OK)


def response_fail(
        enum: Optional[ECEnum] = None,
        desc: Any = '') -> JSONResponse:
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
    content: Dict[str, Any] = dict(code=str(code), error=error, message=message, desc=desc)
    # 响应状态码
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR if code == '500' else status.HTTP_200_OK
    return ExtJsonResponse(content, status_code=status_code)

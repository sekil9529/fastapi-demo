# coding: utf-8

from util.error_code import BaseECEnum, ECData


class ECEnum(BaseECEnum):
    """错误码枚举类"""

    ClientError = ECData(code="400", message="客户端异常")
    InvalidParam = ECData(code="401", message="无效参数")
    ServerError = ECData(code="500", message="服务异常，请稍后重试")


class ECException(Exception):
    """错误码异常类"""

    __slots__ = (
        "enum",
        "message",
    )

    def __init__(self, enum: ECEnum, message: str | None = None):

        self.enum = enum
        self.message = message

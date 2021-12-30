from libs.error_code import BaseECEnum, ECData


class ECEnum(BaseECEnum):
    """错误码枚举类"""

    ServerError = ECData(code="500", message="服务异常，请稍后重试")
    InvalidParam = ECData(code="401", message="无效参数")


class ECException(Exception):
    """错误码异常类"""

    __slots__ = ("enum",)

    def __init__(self, enum: ECEnum):
        self.enum = enum

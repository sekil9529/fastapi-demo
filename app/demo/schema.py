from pydantic import BaseModel, Field

from core.response import ResponseModel


class _HelloResModel(BaseModel):
    """hello响应模型"""
    keyword: str = Field("hello world", title="关键字")


class HelloResModel(ResponseModel):
    """hello响应模式"""

    data: _HelloResModel

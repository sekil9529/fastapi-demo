from pydantic import BaseModel, Field


class HelloResSchema(BaseModel):
    """hello响应模式"""

    keyword: str = Field("hello world", title="关键字")


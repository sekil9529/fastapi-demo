from pydantic import BaseModel, Field


class HelloResSchema(BaseModel):
    """hello响应模式"""

    keyword: str = Field(..., title="关键字", example="hello world")

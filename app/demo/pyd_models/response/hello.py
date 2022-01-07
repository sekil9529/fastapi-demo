"""hello"""

from pydantic import BaseModel, Field


class Model(BaseModel):

    keyword: str = Field(..., title="关键字", example="hello world")

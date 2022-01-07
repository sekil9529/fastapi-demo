from datetime import datetime

from pydantic import BaseModel, Field, validator

from libs.datetime import to_unix_timestamp


class UserModel(BaseModel):
    """用户响应模型"""
    nickname: str = Field("", title="昵称", example="")
    create_time: int = Field(..., title="创建时间", example=0)

    @validator("create_time", pre=True)
    def parse_create_time(cls, value: datetime) -> int:
        return to_unix_timestamp(value)


class Model(BaseModel):
    """用户列表响应模型"""

    user_info_list: list[UserModel]

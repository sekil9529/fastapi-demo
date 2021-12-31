from datetime import datetime

from pydantic import BaseModel, Field


class UserResSchema(BaseModel):
    """用户响应模式"""

    nickname: str = Field("", title="昵称")
    create_time: datetime = Field(..., title="创建时间")


class UserListResSchema(BaseModel):
    """用户列表响应模式"""

    user_info_list: list[UserResSchema]


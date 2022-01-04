from datetime import datetime

from pydantic import BaseModel, Field


class UserResModel(BaseModel):
    """用户响应模型"""
    nickname: str = Field("", title="昵称", example="")
    create_time: datetime = Field(..., title="创建时间", example="")


class UserListResModel(BaseModel):
    """用户列表响应模型"""

    user_info_list: list[UserResModel]

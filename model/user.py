# coding: utf-8

from tortoise import fields
from tortoise.models import Model

__all__ = (
    "User",
)


class User(Model):
    """用户表"""

    class Meta:
        table = "t_user"
        table_description = "用户表"

    id = fields.BigIntField(pk=True, description="表id")
    account = fields.CharField(max_length=50, null=False, description="账号", unique=True)
    avatar = fields.CharField(max_length=255, null=False, default="", description="头像")
    nickname = fields.CharField(max_length=50, null=False, default="", description="昵称")
    password = fields.CharField(max_length=50, null=False, default="", description="密码")
    create_time = fields.DatetimeField(null=False, auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(null=False, auto_now=True, description="更新时间")

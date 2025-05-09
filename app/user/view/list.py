# coding: utf-8

from fastapi import Query
from fastapi.responses import JSONResponse
from tortoise.queryset import ValuesQuery, QuerySet

from app.user.param.response.list import (
    UserModel as UserResModel,
    Model as UserListResModel,
)
from model import User
from util.page import make_page
from helper.response import response_ok


async def user_list(page: int = Query(1, title="页号", ge=1),
                    per_page: int = Query(10, title="每页数量", ge=1, le=10)) -> JSONResponse:
    """用户列表"""

    queryset: QuerySet = make_page(User.filter(), cur_page=page, per_page=per_page)
    value_query: ValuesQuery = queryset.values("nickname", "create_time")
    result: list[dict] = await value_query
    user_info_list: list[UserResModel] = [UserResModel(**item) for item in result]
    data: UserListResModel = UserListResModel(user_info_list=user_info_list)
    return response_ok(data)

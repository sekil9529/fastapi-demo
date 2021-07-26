# coding: utf-8

from typing import List
from fastapi import Request, Body, Query

from sqlalchemy.future import select
from sqlalchemy import desc, update, insert
from app.models import User
from core.response import response_ok
from libs.sqlalchemy.result import result_format
from pydantic import BaseModel, validator

"""
request.headers
request.query_params
request.path_params
body = await request.body()  # 二进制字符串
json_body = await request.json() 
"""


class UserModel(BaseModel):
    name: str = Body(..., min_length=1, max_length=5)


async def add_user(*, request: Request, user_model: UserModel):
    """添加单个用户"""
    session = request.state.db_session
    stmt = insert(User).values(name=user_model.name)
    async with session.begin():
        cur_result = await session.execute(stmt)
        print(cur_result.rowcount)  # 影响的行数
    return response_ok()


class MultiUserModel(BaseModel):
    # 这里的 min_length， max_length 是对每个内部元素的判断
    nameList: List[str] = Body(..., min_length=1, max_length=5)

    @validator('nameList')
    def validate_name_list(cls, value):
        if not value:
            raise ValueError("nameList can't be empty list.")
        if len(value) > 5:
            raise ValueError('nameList out of range.')
        return value


async def batch_add_user(*, request: Request, multi_user_model: MultiUserModel):
    """批量添加用户"""
    values_tuple: tuple = tuple(dict(name=name) for name in multi_user_model.nameList)
    # 注意：.values() 不接受生成器
    # 对应 mysql batch insert
    stmt = insert(User).values(values_tuple)
    db_session = request.state.db_session
    async with db_session.begin():
        cur_result = await db_session.execute(stmt)
        print(cur_result.rowcount)
    return response_ok()


async def user_list(*, request: Request, page: int = Query(default=1, gt=0)):
    """用户列表"""
    per_page = 5
    db_session = request.state.db_session
    query = select(User).select_from(User).order_by(desc(User.ctime), desc(User.id)). \
        offset((page - 1) * per_page).limit(per_page)
    async with db_session.begin():
        cur_result = await db_session.execute(query)
    result = cur_result.fetchall()
    if result:
        result = [objs[0] for objs in result]
    data = result_format(result)
    return response_ok(data)


async def get_user_info(*, request: Request, user_id: int):
    """单个用户信息"""
    db_session = request.state.db_session
    stmt = select(User).select_from(User).where(User.id.in_((user_id, 2, 3, 4)))
    async with db_session.begin():
        cur_result = await db_session.execute(stmt)
    result = cur_result.fetchone()
    if result is None:
        data = {}
    else:
        data = result_format(result[0])
        # data = result[0]
    return response_ok(data)


class UserSetModel(BaseModel):
    name: str = Body(..., min_length=1, max_length=5)


async def set_user_info(*, request: Request, user_id: int, user_set_model: UserSetModel):
    """修改用户信息"""
    db_session = request.state.db_session
    stmt = update(User).where(User.id == user_id)
    if user_set_model.name is not None:
        stmt = stmt.values(name=user_set_model.name)
    async with db_session.begin():
        cur_result = await db_session.execute(stmt)
        print(cur_result.rowcount)
    return response_ok()

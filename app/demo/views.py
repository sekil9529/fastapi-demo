# coding: utf-8

from fastapi import Request

from sqlalchemy.future import select
from app.models import User
from libs.sqlalchemy.result import result_format

"""
request.headers
request.query_params
request.path_params
body = await request.body()  # 二进制字符串
json_body = await request.json() 
"""


async def test(*, request: Request, xxx_id: int):
    # json_body = await request.json()
    session = request.state.db_session
    query = select(User.id, User.ctime).select_from(User).filter(User.id >= 1).limit(10)
    async with session.begin():
        result = await session.execute(query)
    data = result_format(result.fetchall())
    # print(data)
    return {'message': data}


async def test2(request: Request):
    data = 'hello world!'
    return {'message': data}

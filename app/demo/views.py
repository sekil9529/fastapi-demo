# coding: utf-8

from fastapi import Request

from sqlalchemy.future import select
from app.models import User
from ext.error_code import ECEnum
from ext.response import response_ok
from libs.error_code.exception import ECException
from libs.sqlalchemy.result import result_format

"""
request.headers
request.query_params
request.path_params
body = await request.body()  # 二进制字符串
json_body = await request.json() 
"""


async def hello():
    data = 'hello world!'
    return {'message': data}


async def test1(*, request: Request):
    session = request.state.db_session
    query = select(User.name, User.ctime).select_from(User).filter(User.id >= 1).limit(5)
    async with session.begin():
        result = await session.execute(query)
    data = result_format(result.fetchall())
    return response_ok(data)


async def test_error_code():
    raise ECException(ECEnum.TestError)
    return response_ok()

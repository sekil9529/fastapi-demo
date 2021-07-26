# coding: utf-8

from core.error_code import ECEnum
from core.response import response_ok
from libs.error_code.exception import ECException

"""
request.headers
request.query_params
request.path_params
body = await request.body()  # 二进制字符串
json_body = await request.json() 
"""


async def test_hello():
    data = 'hello world!'
    return response_ok(data)


async def test_error_code():
    raise ECException(ECEnum.TestError)
    return response_ok()

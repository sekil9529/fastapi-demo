# coding: utf-8

from core.error_code import ECEnum
from core.response import response_ok
from core.error_code import ECException

"""
request.headers
request.query_params
request.path_params
body = await request.body()  # 二进制字符串
json_body = await request.json() 
"""


async def test_hello():
    """测试hello"""
    data = 'hello world!'
    return response_ok(keyword=data)


async def test_error_code():
    """测试错误码"""
    raise ECException(ECEnum.ServerError)
    return response_ok()

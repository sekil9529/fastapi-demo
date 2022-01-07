from fastapi import Query
from fastapi.responses import JSONResponse

from core.response import response_ok
from app.demo.pyd_models.response.hello import Model as HelloResModel


"""
request.headers
request.query_params
request.path_params
body = await request.body()  # 二进制字符串
json_body = await request.json() 
"""


async def test_hello(keyword: str = Query(..., title="关键字", example="hello world")) -> JSONResponse:
    """测试hello"""

    data: HelloResModel = HelloResModel(keyword=keyword)
    return response_ok(data)

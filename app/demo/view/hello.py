# coding: utf-8

import typing as t

from fastapi import Query
from fastapi.responses import JSONResponse

from helper.response import response_ok
from app.demo.param.response.hello import Model as HelloResModel

if t.TYPE_CHECKING:
    from fastapi.responses import Response


"""
request.headers
request.query_params
request.path_params
body = await request.body()  # 二进制字符串
json_body = await request.json() 
"""


async def test_hello(keyword: str = Query(..., title="关键字", example="hello world")) -> "Response":
    """测试hello"""

    import asyncio
    await asyncio.sleep(3)
    data: HelloResModel = HelloResModel(keyword=keyword)
    return response_ok(data)

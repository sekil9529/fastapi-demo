# coding: utf-8

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.error_code import ECEnum
from core.response import response_ok
from core.error_code import ECException
from .schemas import HelloResSchema

router: APIRouter = APIRouter(prefix="/demo", tags=["demo"])

"""
request.headers
request.query_params
request.path_params
body = await request.body()  # 二进制字符串
json_body = await request.json() 
"""


@router.get("/hello", response_model=HelloResSchema)
async def test_hello() -> JSONResponse:
    """测试hello"""

    keyword: str = 'hello world!'
    data: HelloResSchema = HelloResSchema(keyword=keyword)
    return response_ok(data)


@router.get("/error")
async def test_error_code() -> JSONResponse:
    """测试错误码"""
    raise ECException(ECEnum.ServerError)
    return response_ok()

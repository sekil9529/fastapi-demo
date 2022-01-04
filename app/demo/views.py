from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from core.error_code import ECEnum
from core.response import response_ok
from core.error_code import ECException
from .pyd_models import HelloResSchema
from app.utils.pyd_model import res_model_factory

router: APIRouter = APIRouter(prefix="/demo", tags=["demo"])

"""
request.headers
request.query_params
request.path_params
body = await request.body()  # 二进制字符串
json_body = await request.json() 
"""


@router.get("/hello", response_model=res_model_factory(HelloResSchema))
async def test_hello(keyword: str = Query(..., title="关键字", example="hello world")) -> JSONResponse:
    """测试hello"""

    data: HelloResSchema = HelloResSchema(keyword=keyword)
    return response_ok(data)


@router.get("/error")
async def test_error_code() -> JSONResponse:
    """测试错误码"""
    raise ECException(ECEnum.ServerError)
    return response_ok()

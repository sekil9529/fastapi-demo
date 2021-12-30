# coding: utf-8

from fastapi import APIRouter

from .views import test_hello, test_error_code
from .schema import HelloResModel

# 这里不能写tags，否则文档会多一倍
router = APIRouter(prefix='/demo')


# 路由配置
router.add_api_route(path="/hello", tags=["hello word"], methods=["GET"],
                     endpoint=test_hello, response_model=HelloResModel)
router.add_api_route(path="/error", tags=["错误码"], methods=["GET"],
                     endpoint=test_error_code)


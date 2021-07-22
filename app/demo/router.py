# coding: utf-8

from fastapi import APIRouter

from .views import test_hello, test_error_code

router = APIRouter(prefix='/demo', tags=['示例'])


# 路由配置
router.add_api_route(path='/hello', tags=['hello word'], methods=['GET'], endpoint=test_hello)
router.add_api_route(path='/error', tags=['错误码'], methods=['GET'], endpoint=test_error_code)


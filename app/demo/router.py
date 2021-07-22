# coding: utf-8

from fastapi import APIRouter

from .views import hello, test1, test_error_code

router = APIRouter(prefix='/demo', tags=['示例'])


# 路由配置
router.add_api_route(path='/hello', tags=['hello word'], methods=['GET'], endpoint=hello)
router.add_api_route(path='/test1', tags=['测试1'], methods=['GET'], endpoint=test1)
router.add_api_route(path='/test_error_code', tags=['错误码'], methods=['GET'], endpoint=test_error_code)


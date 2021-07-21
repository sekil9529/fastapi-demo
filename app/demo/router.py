# coding: utf-8

from fastapi import APIRouter

from .views import test, test2

router = APIRouter(prefix='/demo', tags=['示例'])


# 路由配置
router.add_api_route(path='/test2', tags=['测试'], methods=['GET'], endpoint=test2)
router.add_api_route(path='/{xxx_id}', tags=['测试'], methods=['GET'], endpoint=test)


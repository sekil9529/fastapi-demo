# coding: utf-8

from fastapi import APIRouter

from .views import add_user, batch_add_user, user_list, get_user_info, set_user_info

router = APIRouter(prefix='/user', tags=['用户'])


# 路由配置
router.add_api_route(path='/', tags=['新增用户'], methods=['POST'], endpoint=add_user)
router.add_api_route(path='/batch', tags=['批量新增用户'], methods=['POST'], endpoint=batch_add_user)
router.add_api_route(path='/list', tags=['用户列表'], methods=['GET'], endpoint=user_list)
router.add_api_route(path='/{user_id}', tags=['用户信息'], methods=['GET'], endpoint=get_user_info)
router.add_api_route(path='/{user_id}', tags=['修改用户信息'], methods=['PUT'], endpoint=set_user_info)


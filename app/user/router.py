from fastapi import APIRouter

from .view.list import user_list
from app.user.param.response.list import Model as UserListResModel
from helper.response import res_model_factory


router: APIRouter = APIRouter(prefix="/user", tags=["用户"])

# 用户列表
router.add_api_route("/list", user_list, methods=["GET"], response_model=res_model_factory(UserListResModel))

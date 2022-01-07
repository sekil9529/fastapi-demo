from fastapi import APIRouter

from .views import request_self_user_list
from utils.pyd_model import res_model_factory
from app.user.pyd_models.response.list import Model as UserListResModel


router: APIRouter = APIRouter(prefix="/request", tags=["httpx请求"])

# 请求用户列表
router.add_api_route("/self/user/list", request_self_user_list, methods=["GET"],
                     response_model=res_model_factory(res_model_factory(UserListResModel)))

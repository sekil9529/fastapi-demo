from fastapi import APIRouter

from .views.list import user_list
from .pyd_models.response.list import Model as UserListResModel
from app.utils.pyd_model import res_model_factory


router: APIRouter = APIRouter(prefix="/user", tags=["用户"])

# 用户列表
router.add_api_route("/list", user_list, methods=["GET"], response_model=res_model_factory(UserListResModel))

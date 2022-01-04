from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from tortoise.queryset import ValuesQuery, QuerySet

from .pyd_models import UserResModel, UserListResModel
from app.models import User
from app.utils.page import make_page
from core.response import response_ok
from app.utils.pyd_model import res_model_factory

router: APIRouter = APIRouter(prefix="/user", tags=["用户"])


@router.get(path="/list", response_model=res_model_factory(UserListResModel))
async def user_list(page: int = Query(1, title="页号", ge=1),
                    per_page: int = Query(10, title="每页数量")) -> JSONResponse:
    """用户列表"""

    queryset: QuerySet = make_page(User.filter(), cur_page=page, per_page=per_page)
    value_query: ValuesQuery = queryset.values("nickname", "create_time")
    result: list[dict] = await value_query
    user_info_list: list[UserResModel] = [UserResModel(**item) for item in result]
    data: UserListResModel = UserListResModel(user_info_list=user_info_list)
    return response_ok(data)

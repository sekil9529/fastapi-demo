from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from tortoise.queryset import ValuesQuery, QuerySet

from .schemas import UserResSchema, UserListResSchema
from app.models import User
from app.utils.page import make_page
from core.response import response_ok

router: APIRouter = APIRouter(prefix="/user", tags=["用户"])


@router.get(path="/list", response_model=UserListResSchema)
async def user_list(page: int = Query(1, title="页号", ge=1),
                    per_page: int = Query(10, title="每页数量")) -> JSONResponse:
    """用户列表"""

    queryset: QuerySet = make_page(User.filter(), cur_page=page, per_page=per_page)
    value_query: ValuesQuery = queryset.values("nickname", "create_time")
    result: list[dict] = await value_query
    user_info_list: list[UserResSchema] = [UserResSchema(**item) for item in result]
    data: UserListResSchema = UserListResSchema(user_info_list=user_info_list)
    return response_ok(data)

from typing import Any

import httpx
from fastapi.requests import Request
from starlette.responses import JSONResponse

from core.events.test_request import TEST_REQ_CLIENT
from core.response import response_ok


async def request_self_user_list(request: Request) -> JSONResponse:
    """请求自己的用户列表

    仅 httpx 使用示例
    """
    test_client: httpx.AsyncClient = getattr(request.app.state, TEST_REQ_CLIENT)
    params: dict[str, Any] = {
        "page": 1,
        "per_page": 2
    }
    response: httpx.Response = await test_client.get(url="/user/list", params=params)
    return response_ok(response.json())

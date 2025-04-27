# coding: utf-8

import logging
import typing as t

from starlette.middleware.base import BaseHTTPMiddleware

if t.TYPE_CHECKING:
    from starlette.types import ASGIApp
    from fastapi import Request, Response
    from starlette.middleware.base import RequestResponseEndpoint, DispatchFunction


_KEYS: set[str] = set()


class BaseMiddleware(BaseHTTPMiddleware):
    """中间件基类"""

    _KEY: str | None = None

    def __init__(self,
                 app: "ASGIApp",
                 dispatch: "DispatchFunction" = None) -> None:

        if self._KEY is not None:
            assert self._KEY not in _KEYS, f"Duplicate middleware key: {self._KEY}"
            _KEYS.add(self._KEY)
        super(BaseMiddleware, self).__init__(app, dispatch)
        self._logger = logging.getLogger(f"middleware.{self.__class__.__name__}")

    async def before_request(self, request: "Request") -> None:
        """请求执行前"""

        raise NotImplementedError

    async def before_response(self, request: "Request", response: "Response") -> None:
        """请求执行后返回前"""

        raise NotImplementedError

    async def dispatch(self, request: "Request", call_next: "RequestResponseEndpoint") -> "Response":
        """调度"""

        await self.before_request(request)
        response = await call_next(request)
        await self.before_response(request, response)
        return response

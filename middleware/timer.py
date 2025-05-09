# coding: utf-8

import time
import typing as t

from .base import BaseMiddleware
from setting import Setting

if t.TYPE_CHECKING:
    from fastapi import Request, Response


class TimeOutMiddleware(BaseMiddleware):
    """超时中间件"""

    _KEY = "start_time"

    async def before_request(self, request: "Request") -> None:

        setattr(request.state, self._KEY, time.time())

    async def before_response(self, request: "Request", response: "Response") -> None:

        diff = time.time() - getattr(request.state, self._KEY)
        if diff > Setting.UD_SLOW_TIMEOUT:
            self._logger.warning('response timeout: %.6f' % diff)

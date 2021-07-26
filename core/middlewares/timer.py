# coding: utf-8

import time
from contextvars import ContextVar, Token
from starlette.requests import Request
from starlette.responses import Response
from loguru import logger

from .base import BaseMiddleware


class TimerMiddleware(BaseMiddleware):

    threshold: float = 1.0
    time_var: ContextVar = ContextVar('time')

    async def before_request(self, request: Request) -> None:
        request.state.time_token = self.time_var.set(time.time())

    async def before_response(self, request: Request, response: Response) -> None:
        if hasattr(request.state, 'time_token'):
            diff = time.time() - self.time_var.get()
            if diff > self.threshold:
                logger.warning('response timeout: %.6f' % diff)
            self.time_var.reset(request.state.time_token)

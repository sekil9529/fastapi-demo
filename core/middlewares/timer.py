# coding: utf-8

import time
from starlette.requests import Request
from starlette.responses import Response
from loguru import logger

from .base import BaseMiddleware


class TimerMiddleware(BaseMiddleware):

    threshold: float = 1.0

    async def before_request(self, request: Request) -> None:
        request.state.start_time = time.time()

    async def before_response(self, request: Request, response: Response) -> None:
        key: str = 'start_time'
        if hasattr(request.state, key):
            diff: float = time.time() - getattr(request.state, key)
            if diff > self.threshold:
                logger.warning('response timeout: %.6f' % diff)

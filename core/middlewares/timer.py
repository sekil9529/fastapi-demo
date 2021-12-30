import time

from starlette.requests import Request
from starlette.responses import Response

from .base import BaseMiddleware
from libs.logger import LoggerProxy

# 阈值
TIME_THRESHOLD: float = 1.0
# 关键字
TIME_KEY: str = "start_time"

logger: LoggerProxy = LoggerProxy(__name__)


class TimeOutMiddleware(BaseMiddleware):
    """超时中间件"""

    async def before_request(self, request: Request) -> None:
        setattr(request.state, TIME_KEY, time.time())

    async def before_response(self, request: Request, response: Response) -> None:
        if hasattr(request.state, TIME_KEY):
            diff = time.time() - getattr(request.state, TIME_KEY)
            if diff > TIME_THRESHOLD:
                logger.warning('response timeout: %.6f' % diff)

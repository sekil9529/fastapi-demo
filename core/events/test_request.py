import httpx

from .base import BaseEvent
from libs.logger import LoggerProxy

logger: LoggerProxy = LoggerProxy(__name__)

TEST_REQ_CLIENT: str = "test_req_client"


class TestRequestEvent(BaseEvent):
    """测试请求事件"""

    async def on_startup(self):
        test_url: str = self._app.state.settings.UD_TEST_URL
        client: httpx.AsyncClient = httpx.AsyncClient(base_url=test_url, timeout=3)
        setattr(self._app.state, TEST_REQ_CLIENT, client)
        logger.info("Bind test-request-client.")

    async def on_shutdown(self):
        if hasattr(self._app.state, TEST_REQ_CLIENT):
            await getattr(self._app.state, TEST_REQ_CLIENT).aclose()
            logger.info("Ensure test-request-client close transport and proxies.")

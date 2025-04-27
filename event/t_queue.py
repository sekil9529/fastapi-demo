# coding: utf-8

from event.base import BaseEvent
from extra.app_proxy import AppProxy
from helper.t_queue import TestQueue

__all__ = (
    "test_queue_proxy",
    "TestQueueEvent",
)

test_queue_proxy: AppProxy["TestQueue"] = AppProxy("test_queue")


class TestQueueEvent(BaseEvent):
    """测试事件"""

    async def on_startup(self):

        obj = TestQueue()
        test_queue_proxy.bind_obj(self._app, obj)
        self._logger.info("test queue bind done.")

    async def on_shutdown(self):

        obj = test_queue_proxy.get_obj()
        await obj.close()
        self._logger.info("test queue close done.")

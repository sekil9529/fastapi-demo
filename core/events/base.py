from fastapi import FastAPI
from starlette.datastructures import State


class BaseEvent:
    """事件基类"""

    __slots__ = ('_app', 'state')

    def __init__(self, app: FastAPI):
        self._app = app
        self.state = State()

    async def on_startup(self):
        raise NotImplementedError

    async def on_shutdown(self):
        raise NotImplementedError

# coding: utf-8

import logging
import typing as t

from starlette.datastructures import State

if t.TYPE_CHECKING:
    from fastapi import FastAPI


_KEYS: set[str] = set()


class BaseEvent:
    """事件基类"""

    __slots__ = (
        "_app",
        "_state",
        "_logger",
    )

    def __init__(self, app: "FastAPI"):

        self._app = app
        self._state = State()
        self._logger = logging.getLogger(f"event.{self.__class__.__name__}")

    async def on_startup(self):

        raise NotImplementedError

    async def on_shutdown(self):

        raise NotImplementedError

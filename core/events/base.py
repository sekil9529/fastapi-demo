# coding: utf-8

import abc
from fastapi import FastAPI
from types import SimpleNamespace

from settings.base import BaseSettings


class BaseEvent(metaclass=abc.ABCMeta):
    """事件基类"""

    __slots__ = ('_app', '_settings', 'ext')

    def __init__(self, app: FastAPI, settings: BaseSettings):
        self._app = app
        self._settings = settings
        self.ext = SimpleNamespace()  # 扩展

    @abc.abstractmethod
    async def on_startup(self):
        pass

    @abc.abstractmethod
    async def on_shutdown(self):
        pass

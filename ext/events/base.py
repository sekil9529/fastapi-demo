# coding: utf-8

import abc
from fastapi import FastAPI

from settings.base import BaseSettings
from libs.dict import ExtDict


class BaseEvent(metaclass=abc.ABCMeta):
    """基础事件"""

    __slots__ = ('_app', '_settings', 'ext')

    def __init__(self, app: FastAPI, settings: BaseSettings):
        self._app = app
        self._settings = settings
        self.ext = ExtDict()  # 扩展

    @abc.abstractmethod
    async def on_startup(self):
        pass

    @abc.abstractmethod
    async def on_shutdown(self):
        pass

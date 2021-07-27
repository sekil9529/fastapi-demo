# coding: utf-8

import abc
from typing import Optional, Type
from starlette.responses import JSONResponse


class BaseHandler(metaclass=abc.ABCMeta):

    __slots__ = ()

    @abc.abstractmethod
    def get_exception(self) -> Type[Exception]:
        """创建exception"""
        pass

    @abc.abstractmethod
    async def exc_handler(self, request, exc: Exception) -> JSONResponse:
        """异常处理"""
        pass

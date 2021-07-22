# coding: utf-8

import abc
from typing import Optional, Type
from starlette.responses import JSONResponse


class BaseHandler(metaclass=abc.ABCMeta):

    __slots__ = ()

    _exception: Optional[Exception] = None

    @abc.abstractmethod
    def get_exception(self) -> Type[Exception]:
        """创建exception"""
        pass

    @abc.abstractmethod
    async def exc_handler(self, request, exc: Exception) -> JSONResponse:
        """异常处理"""
        pass

    @property
    def exception(self):
        """获取exception类"""
        if self.__class__._exception is None:
            self.__class__._exception = self.get_exception()
        return self.__class__._exception

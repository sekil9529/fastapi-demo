from typing import Optional
from starlette.responses import JSONResponse


class BaseHandler():

    __slots__ = ()

    def get_exception(self) -> type[Exception]:
        """获取异常类"""
        raise NotImplementedError

    async def exc_handler(self, request, exc: Exception) -> JSONResponse:
        """异常处理"""
        raise NotImplementedError

    @property
    def exception(self) -> type[Exception]:
        """获取exception类"""
        return self.get_exception()

# coding: utf-8

import logging
import typing as t

if t.TYPE_CHECKING:
    from fastapi.requests import Request
    from fastapi.responses import Response


class BaseHandler:

    __slots__ = (
        "_logger",
    )

    def __init__(self):

        self._logger = logging.getLogger(self.__class__.__name__)

    def get_exception(self) -> type["Exception"]:  # pragma: no cover
        """获取异常类"""

        raise NotImplementedError

    async def exc_handler(self, request: "Request", exc: Exception) -> "Response":  # pragma: no cover
        """异常处理"""

        raise NotImplementedError

    @property
    def exception(self) -> type[Exception]:
        """获取exception类"""

        return self.get_exception()

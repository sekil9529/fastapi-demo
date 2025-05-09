# coding: utf-8

"""请求中间件"""

import typing as t

from middleware.timer import TimeOutMiddleware

if t.TYPE_CHECKING:
    from middleware.base import BaseMiddleware


MIDDLEWARES: list[type["BaseMiddleware"]] = [
    TimeOutMiddleware,
]

# coding: utf-8

from .base import BaseMiddleware
from .timer import TimeOutMiddleware


MIDDLEWARES: list[type[BaseMiddleware]] = [
    TimeOutMiddleware,
]

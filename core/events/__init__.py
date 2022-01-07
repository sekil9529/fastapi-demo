# coding: utf-8

from .base import BaseEvent
from .test_request import TestRequestEvent


EVENTS: list[type[BaseEvent]] = [
    TestRequestEvent,
]

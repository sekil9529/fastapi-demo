# coding: utf-8

"""事件"""

import typing as t

from event.t_queue import TestQueueEvent

if t.TYPE_CHECKING:
    from event.base import BaseEvent


EVENTS: list[type["BaseEvent"]] = [
    TestQueueEvent,
]

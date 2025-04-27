# coding: utf-8

import logging
import typing as t
from contextvars import ContextVar
from dataclasses import dataclass, field

__all__ = (
    "record_proxy",
    "PyLogRecord",
)

# 用于临时存储日志记录数据
_RECORD_LOCAL: ContextVar = ContextVar("record_local")


@dataclass()
class _RecordData:
    """数据"""

    path: str = field(default="<path>")
    method: str = field(default="<method>")


if t.TYPE_CHECKING:
    _RecordBase = _RecordData
else:
    _RecordBase = object


class _RecordProxy(_RecordBase):

    __slots__ = (
        "_local",
    )

    def __init__(self):
        self._local = _RECORD_LOCAL

    def _get_value(self) -> "_RecordData":
        """获取上下文变量"""

        return self._local.get(_RecordData())

    def _set_value(self, value: "_RecordData") -> None:
        """设置上下文变量"""

        self._local.set(value)

    def __getattr__(self, item):

        value = self._get_value()
        return getattr(value, item)


record_proxy = _RecordProxy()


class PyLogRecord(logging.LogRecord):
    """扩展的LogRecord"""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.path = record_proxy.path
        self.method = record_proxy.method

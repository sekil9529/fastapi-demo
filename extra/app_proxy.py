# coding: utf-8

"""应用级代理"""

import typing as t

if t.TYPE_CHECKING:  # pragma: no cover
    from fastapi.applications import FastAPI

__all__ = (
    "AppProxy",
)

_T = t.TypeVar("_T")
_KEYS: set[str] = set()


class AppProxy(t.Generic[_T]):
    """应用代理"""

    def __init__(self, key_name: str):

        assert key_name not in _KEYS, f"key_name: {key_name} already exist"
        _KEYS.add(key_name)
        self._key_name = key_name
        self._app: t.Optional["FastAPI"] = None

    def bind_obj(self, app: "FastAPI", obj: _T) -> None:
        """设置对象"""

        self._app = app
        setattr(self._app.state, self._key_name, obj)

    def get_obj(self) -> _T:
        """获取对象"""

        obj: _T | None = getattr(self._app.state, self._key_name, None)
        if obj is None:
            raise ValueError("object not exist")
        return obj

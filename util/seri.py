# coding: utf-8

"""序列化"""

import typing as t

import orjson


__all__ = (
    "json_dumps",
    "json_loads",
)


_DefaultType = t.Callable[[t.Any], t.Any] | None


# @t.overload
# def json_dumps(data: t.Any, *, default: _DefaultType, return_bytes: t.Literal[True]) -> bytes: ...
# @t.overload
# def json_dumps(data: t.Any, *, default: _DefaultType, return_bytes: t.Literal[False]) -> str: ...


def json_dumps(data: t.Any, *, default: _DefaultType = None, return_bytes: bool = False) -> str | bytes:

    result: bytes = orjson.dumps(data, default=default)
    if return_bytes:
        return result
    return result.decode("utf-8")


def json_loads(data: str | bytes) -> t.Any:

    return orjson.loads(data)

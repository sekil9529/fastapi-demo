# coding: utf-8

import typing as t

from fastapi.responses import JSONResponse as _JSONResponse

from util.seri import json_dumps


__all__ = (
    "JSONResponse",
)


class JSONResponse(_JSONResponse):
    """

    支持直接传递 bytes 类型的响应内容
    """

    def render(self, content: t.Any) -> bytes:

        if isinstance(content, bytes):
            return content
        return json_dumps(content, return_bytes=True)

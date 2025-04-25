# coding: utf-8

import typing as t

from fastapi.requests import Request as _Request

from util.seri import json_loads

__all__ = (
    "Request",
)


class Request(_Request):

    async def json(self) -> t.Any:

        if not hasattr(self, "_json"):
            body = await self.body()
            self._json = json_loads(body)
        return self._json

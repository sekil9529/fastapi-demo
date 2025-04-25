# coding: utf-8

import typing as t

import fastapi
from fastapi.applications import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.exceptions import ExceptionMiddleware

if t.TYPE_CHECKING:  # pragma: no cover
    from starlette.types import ASGIApp
    from fastapi.requests import Request
    from fastapi.responses import Response


__all__ = (
    "FastAPI",
)


if fastapi.__version__ == "0.112.0":

    """修复Exception异常处理，无法使用 await request.body()"""

    class FastAPI(FastAPI):

        def build_middleware_stack(self) -> "ASGIApp":
            debug = self.debug
            exception_handlers: dict[
                t.Any, t.Callable[[Request, Exception], Response]
            ] = {}

            for key, value in self.exception_handlers.items():
                exception_handlers[key] = value

            middleware = (
                    self.user_middleware
                    + [
                        Middleware(
                            ExceptionMiddleware, handlers=exception_handlers, debug=debug
                        )
                    ]
            )
            app = self.router
            for cls, args, kwargs in reversed(middleware):
                app = cls(app=app, *args, **kwargs)
            return app

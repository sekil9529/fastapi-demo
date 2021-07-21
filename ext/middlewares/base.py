# coding: utf-8

import abc
from fastapi import FastAPI
from fastapi import Request, Response
from starlette.types import ASGIApp
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint, DispatchFunction


class BaseMiddleware(BaseHTTPMiddleware, metaclass=abc.ABCMeta):

    def __init__(self,
                 app: ASGIApp,
                 fast_api_app: FastAPI,
                 dispatch: DispatchFunction = None) -> None:
        super(BaseMiddleware, self).__init__(app, dispatch)
        self.fast_api_app = fast_api_app

    @abc.abstractmethod
    async def before_request(self, request: Request) -> None:
        """请求执行前"""
        pass

    @abc.abstractmethod
    async def before_response(self, request: Request, response: Response) -> None:
        """请求执行后返回前"""
        pass

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """调度"""
        await self.before_request(request)
        response = await call_next(request)
        await self.before_response(request, response)
        return response

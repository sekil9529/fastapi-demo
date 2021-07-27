# coding: utf-8

from fastapi import Request, Response

from .base import BaseMiddleware


class SQLAlchemyMiddleware(BaseMiddleware):
    """sqlalchemy中间件"""

    async def before_request(self, request: Request) -> None:
        request.state.db_session = self.fast_api_app.state.DBSession()

    async def before_response(self, request: Request, response: Response) -> None:
        key: str = 'db_session'
        if hasattr(request.state, key):
            await getattr(request.state, key).close()

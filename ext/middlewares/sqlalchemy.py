# coding: utf-8

from contextvars import ContextVar
from fastapi import Request, Response

from .base import BaseMiddleware


class SQLAlchemyMiddleware(BaseMiddleware):
    """sqlalchemy中间件"""

    # db_session_token: ContextVar = ContextVar('database session')

    async def before_request(self, request: Request) -> None:
        request.state.db_session = self.fast_api_app.state.DBSession()
        # request.state.db_session_token = self.db_session_token.set(request.state.db_session)

    async def before_response(self, request: Request, response: Response) -> None:
        # if hasattr(request.state, "db_session_token"):
        #     self.db_session_token.reset(request.state.db_session_token)
        #     await request.state.db_session.close()
        if hasattr(request.state, 'db_session'):
            await request.state.db_session.close()

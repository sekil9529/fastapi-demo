# coding: utf-8

from .base import BaseEvent
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


class SQLAlchemyEvent(BaseEvent):
    """SQLAlchemy事件"""

    async def on_startup(self):
        """app绑定BDSession"""
        self.ext.engine = create_async_engine(self._settings.SQLALCHEMY_DATABASE_URL, echo=False,
                                              **self._settings.SQLALCHEMY_ENGINE_OPTIONS)
        self._app.state.DBSession = sessionmaker(self.ext.engine, expire_on_commit=False, class_=AsyncSession)

    async def on_shutdown(self):
        """释放连接池"""
        await self.ext.engine.dispose()

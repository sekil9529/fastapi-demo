# coding: utf-8

import typing as t

from tortoise.backends.mysql import MySQLClient as _MySQLClient
from tortoise.backends.base.client import PoolConnectionWrapper

if t.TYPE_CHECKING:
    from tortoise.backends.base.client import T_conn


class _AutoReconnectWrapperProxy:

    def __init__(self, wrapper: "PoolConnectionWrapper"):

        self._wrapper = wrapper

    def __getattr__(self, item):

        return getattr(self._wrapper, item)

    async def __aenter__(self) -> "T_conn":

        conn = await self._wrapper.__aenter__()
        conn.ping(reconnect=True)
        return conn


class _AutoReconnectMySQLClient(_MySQLClient):
    """自动重连

    牺牲部分性能，防止网络原因导致连接异常断开
    """

    def acquire_connection(self) -> "PoolConnectionWrapper":

        wrapper = super().acquire_connection()
        proxy = _AutoReconnectWrapperProxy(wrapper)
        return t.cast(PoolConnectionWrapper, proxy)


client_class = _AutoReconnectMySQLClient

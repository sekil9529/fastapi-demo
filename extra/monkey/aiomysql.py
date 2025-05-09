# coding: utf-8

import sys
import typing as t

from aiomysql.pool import Pool as _Pool

if t.TYPE_CHECKING:
    from aiomysql.connection import Connection


__all__ = (
    "patch_auto_reconnect_pool",
)


class _AutoReconnectPool(_Pool):
    """自动重连

    牺牲部分性能，保证连接池的连接不会因为网络波动而断开
    """

    async def _acquire(self):

        conn: "Connection" = await super()._acquire()
        await conn.ping(reconnect=True)
        return conn


def patch_auto_reconnect_pool() -> None:
    """连接池补丁"""

    setattr(sys.modules["aiomysql"], "Pool", _AutoReconnectPool)
    setattr(sys.modules["aiomysql.pool"], "Pool", _AutoReconnectPool)

import sys

from aiomysql.connection import Connection
from aiomysql.pool import Pool as OriginPool


class Pool(OriginPool):

    async def _acquire(self):
        conn: Connection = await super(Pool, self)._acquire()
        await conn.ping()
        return conn


def patch_pool() -> None:
    """连接池补丁"""
    setattr(sys.modules["aiomysql"], "Pool", Pool)
    setattr(sys.modules["aiomysql.pool"], "Pool", Pool)

# coding: utf-8

import typing as t

if t.TYPE_CHECKING:
    from fastapi import APIRouter

from app.demo.router import router as demo_router
from app.user.router import router as user_router

# 路由
ROUTERS: list["APIRouter"] = [
    demo_router,
    user_router,
]

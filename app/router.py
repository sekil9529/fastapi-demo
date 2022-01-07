from fastapi import APIRouter

from .demo.router import router as demo_router
from .user.router import router as user_router

# 路由
ROUTERS: list[APIRouter] = [
    demo_router,
    user_router,
]

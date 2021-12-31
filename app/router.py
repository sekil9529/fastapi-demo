from fastapi import APIRouter

from .demo.views import router as demo_router
from .user.views import router as user_router

# 路由
ROUTERS: list[APIRouter] = [
    demo_router,
    user_router,
]

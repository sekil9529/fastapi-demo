# coding: utf-8

from .demo.router import router as demo_router
from .user.router import router as user_router

ROUTER_TUPLE = (
    demo_router,
    user_router,
)

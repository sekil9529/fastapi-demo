from fastapi import APIRouter

from .demo.router import router as demo_router

ROUTERS: list[APIRouter] = [
    demo_router,
]

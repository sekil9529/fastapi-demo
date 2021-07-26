# coding: utf-8

import os
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings import get_settings
from settings.base import BaseSettings
from core.events import EVENT_TUPLE
from core.middlewares import MIDDLEWARE_TUPLE
from core.exception_handlers import EXC_HDL_TUPLE
from app.router import ROUTER_TUPLE
from libs.logger import init_log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_app(env: Optional[str] = None) -> FastAPI:
    """创建app

    :param env: None, env, pro
    :return: FastAPI
    """

    # 初始化日志
    init_log(BASE_DIR)

    # 获取配置
    settings = get_settings(env)

    # 创建app
    app = FastAPI(
        ebug=settings.DEBUG,
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        openapi_url=settings.OPENAPI_URL,
        redoc_url=settings.REDOC_URL
    )

    # 事件
    register_event(app, settings)
    # cors
    register_cors(app)
    # 自定义中间件
    register_udf_middleware(app)
    # 异常捕获
    register_exception_handler(app)
    # router
    register_router(app)

    return app


def register_event(app: FastAPI, settings: BaseSettings) -> None:
    """注册事件"""

    for event_cls in EVENT_TUPLE:
        event = event_cls(app, settings)
        if hasattr(event, 'on_startup'):
            app.add_event_handler('startup', event.on_startup)
        if hasattr(event, 'on_shutdown'):
            app.add_event_handler('shutdown', event.on_shutdown)
    return None


def register_udf_middleware(app: FastAPI) -> None:
    """注册自定义中间件"""
    for middleware_cls in MIDDLEWARE_TUPLE:
        # 参考 app.middlewares('http')
        app.add_middleware(middleware_cls, fast_api_app=app)
    return None


def register_router(app: FastAPI, prefix: Optional[str] = '/api') -> None:
    """注册router"""
    if prefix is None:
        prefix = ''
    for router_ in ROUTER_TUPLE:
        app.include_router(router_, prefix=prefix)
    return None


def register_cors(app: FastAPI) -> None:
    """注册cors"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )


def register_exception_handler(app: FastAPI) -> None:
    """注册异常捕获"""
    for exc_hdl_cls in EXC_HDL_TUPLE:
        exc_hdl = exc_hdl_cls()
        app.add_exception_handler(exc_hdl.exception, exc_hdl.exc_handler)
    return None

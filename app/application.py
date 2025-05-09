# coding: utf-8

import logging
from logging.config import dictConfig

from fastapi import FastAPI
# from extra.fastapi.app import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from setting import Setting
from event import EVENTS
from middleware import MIDDLEWARES
from exception_handler import EXCEPTION_HANDLERS
from app.router import ROUTERS
from util.log_record import PyLogRecord


_LOGGER = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """创建app

    :return: FastAPI
    """

    """配置日志"""
    logging.setLogRecordFactory(PyLogRecord)
    dictConfig(Setting.LOGGING)

    """创建应用"""
    app: "FastAPI" = FastAPI(
        debug=Setting.DEBUG,
        title=Setting.TITLE,
        description=Setting.DESCRIPTION,
        docs_url=Setting.DOCS_URL,
        openapi_url=Setting.OPENAPI_URL,
        redoc_url=Setting.REDOC_URL,
    )

    """事件"""
    # 自定义事件
    _register_event(app)
    # 注册tortoise
    register_tortoise(app, config=Setting.TORTOISE, generate_schemas=False)

    """中间件"""
    # cors
    _register_cors(app)
    # 请求中间件
    _register_request_middleware(app)

    """异常捕获"""
    _register_exception_handler(app)

    """路由"""
    _register_router(app)

    return app


def _register_event(app: "FastAPI") -> None:
    """注册事件"""

    for event_cls in EVENTS:
        event = event_cls(app)
        app.add_event_handler('startup', event.on_startup)
        app.add_event_handler('shutdown', event.on_shutdown)


def _register_request_middleware(app: "FastAPI") -> None:
    """注册请求中间件"""

    for middleware_cls in MIDDLEWARES:
        # 参考 app.middleware('http')
        app.add_middleware(middleware_cls)


def _register_router(app: "FastAPI", prefix: str | None = '/api') -> None:
    """注册router"""

    if prefix is None:
        prefix = ""
    for router_ in ROUTERS:
        app.include_router(router_, prefix=prefix)


def _register_cors(app: "FastAPI") -> None:
    """注册cors"""

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )


def _register_exception_handler(app: "FastAPI") -> None:
    """注册异常捕获"""

    for exc_hdl_cls in EXCEPTION_HANDLERS:
        exc_hdl = exc_hdl_cls()
        app.add_exception_handler(exc_hdl.exception, exc_hdl.exc_handler)

from typing import Optional
from logging.config import dictConfig

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from settings import Settings
from core.events import EVENTS
from core.middlewares import MIDDLEWARES
from core.exception_handlers import EXCEPTION_HANDLERS
from app.router import ROUTERS


def create_app() -> FastAPI:
    """创建app

    :return: FastAPI
    """

    # 配置日志
    dictConfig(Settings.LOGGING)

    # 创建app
    app = FastAPI(
        ebug=Settings.DEBUG,
        title=Settings.TITLE,
        description=Settings.DESCRIPTION,
        docs_url=Settings.DOCS_URL,
        openapi_url=Settings.OPENAPI_URL,
        redoc_url=Settings.REDOC_URL
    )
    # 绑定设置
    app.state.settings = Settings

    # 事件
    register_event(app)

    # 注册tortoise
    register_tortoise(app, config=Settings.TORTOISE, generate_schemas=False)

    # cors
    register_cors(app)
    # 自定义中间件
    register_udf_middleware(app)
    # 异常捕获
    register_exception_handler(app)
    # router
    register_router(app)

    return app


def register_event(app: FastAPI) -> None:
    """注册事件"""

    for event_cls in EVENTS:
        event = event_cls(app)
        if hasattr(event, 'on_startup'):
            app.add_event_handler('startup', event.on_startup)
        if hasattr(event, 'on_shutdown'):
            app.add_event_handler('shutdown', event.on_shutdown)


def register_udf_middleware(app: FastAPI) -> None:
    """注册自定义中间件"""
    for middleware_cls in MIDDLEWARES:
        # 参考 app.middlewares('http')
        app.add_middleware(middleware_cls)


def register_router(app: FastAPI, prefix: Optional[str] = '/api') -> None:
    """注册router"""
    if prefix is None:
        prefix = ""
    for router_ in ROUTERS:
        app.include_router(router_, prefix=prefix)


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
    for exc_hdl_cls in EXCEPTION_HANDLERS:
        exc_hdl = exc_hdl_cls()
        app.add_exception_handler(exc_hdl.exception, exc_hdl.exc_handler)

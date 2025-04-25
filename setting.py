# coding: utf-8

import os
import typing as t

from helper.config import Config
from util.py_yaml import PyYaml


class Setting:
    """配置类"""

    _BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _LOG_DIR = os.path.join(_BASE_DIR, "log")
    _CONFIG_DIR = os.path.join(_BASE_DIR, "config")

    # 配置
    CONFIG = Config(**PyYaml(os.path.join(_CONFIG_DIR, "config.yaml")).to_dict())

    DEBUG: bool = CONFIG.server.debug
    TITLE: str = "demoFastAPI"
    DESCRIPTION: str = "FastAPI Demo"

    # 文档地址 默认为docs
    DOCS_URL: str | None = "/api/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str | None = "/api/openapi.json"
    # redoc 文档
    REDOC_URL: str | None = "/api/redoc"

    # 日志配置
    LOGGING: dict[str, t.Any] = {
        "version": 1,
        "loggers": {
            "": {
                "level": "INFO",
                "handlers": ["console", "info_file", "error_file"],
                "propagate": False
            },
            "fastapi": {
                "level": "INFO",
                "handlers": ["console", "info_file", "error_file"],
                "propagate": False
            },
            "uvicorn": {
                "level": "INFO",
                "handlers": ["console", "info_file", "error_file"],
                "propagate": False
            },
        },
        "formatters": {
            "default": {
                "format": "[%(asctime)s.%(msecs).3d] - [%(levelname)s] - [%(name)s:%(lineno)d] - [%(message)s]",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "default",
            },
            "info_file": {
                "class": "concurrent_log_handler.ConcurrentRotatingFileHandler",
                "filename": os.path.join(_LOG_DIR, "info.log"),
                "maxBytes": 1024 * 1024 * 32,
                "backupCount": 1,
                "encoding": "utf8",
                "level": "INFO",
                "formatter": "default",
            },
            "error_file": {
                "class": "concurrent_log_handler.ConcurrentRotatingFileHandler",
                "filename": os.path.join(_LOG_DIR, "error.log"),
                "maxBytes": 1024 * 1024 * 128,
                "backupCount": 5,
                "encoding": "utf8",
                "level": "ERROR",
                "formatter": "default",
            },
        },
    }

    # tortoise
    TORTOISE: dict[str, t.Any] = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.mysql",
                "credentials": {
                    "host": CONFIG.db.host,
                    "port": CONFIG.db.port,
                    "user": CONFIG.db.user,
                    "password": CONFIG.db.password,
                    "database": CONFIG.db.database,
                    "maxsize": 2,
                    # 注意：启动时直接创建2个session
                    "minsize": 2,
                    # 回收时间，每次获取session时判断，如果超时，全部重新创建
                    "pool_recycle": 60 * 60 * 2,
                    # 设置事务隔离级别为RC
                    "init_command": "SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED",
                }
            }
        },
        "app": {
            "models": {
                "models": ["models"],
                "default_connection": "default",
            }
        },
        "use_tz": False,
        # set session time_zone
        "timezone": "Asia/Shanghai",
    }

    # 自定义参数
    UD_TEST_URL: str = CONFIG.request.test_url

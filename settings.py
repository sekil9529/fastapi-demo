from typing import Optional, Any

import os

from libs.config import Config

# 项目根路径
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志文件路径
LOG_PATH: str = os.path.join(BASE_DIR, "logs")

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

# 配置
CONF: Config = Config(".env")


class Settings:
    """配置类"""

    DEBUG: bool = bool(int(CONF.server.debug))

    TITLE: str = "demoFastAPI"
    DESCRIPTION: str = "FastAPI Demo"

    # 文档地址 默认为docs
    DOCS_URL: Optional[str] = "/api/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: Optional[str] = "/api/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/api/redoc"

    # 日志配置
    LOGGING: dict[str, Any] = {
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
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(LOG_PATH, "info.log"),
                "maxBytes": 5 * 1024 * 1024,
                "backupCount": 10,
                "encoding": "utf8",
                "level": "INFO",
                "formatter": "default",
            },
            "error_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(LOG_PATH, "error.log"),
                "maxBytes": 5 * 1024 * 1024,
                "backupCount": 10,
                "encoding": "utf8",
                "level": "ERROR",
                "formatter": "default",
            },
        },
    }

    # tortoise
    TORTOISE: dict[str, Any] = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.mysql",
                "credentials": {
                    "host": CONF.db.host,
                    "port": CONF.db.port,
                    "user": CONF.db.user,
                    "password": CONF.db.password,
                    "database": CONF.db.database,
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
        "apps": {
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
    UD_TEST_URL: str = CONF.request.test_url

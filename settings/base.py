# coding: utf-8

import os
from typing import Optional, Dict, Any
from pydantic import BaseSettings as BSettings

from libs.config import Config

# 项目根路径
BASE_DIR: str = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

# 配置信息
CONFIG_INFO = Config(os.path.join(BASE_DIR, '.env')).format()


class BaseSettings(BSettings):
    """基类"""

    DEBUG: bool = True

    # 项目文档
    TITLE: str
    DESCRIPTION: str

    # 文档地址 默认为docs
    DOCS_URL: Optional[str]
    # 文档关联请求数据接口
    OPENAPI_URL: Optional[str]
    # redoc 文档
    REDOC_URL: Optional[str]

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URL: str
    # SQLAlchemy其他参数
    SQLALCHEMY_ENGINE_OPTIONS: Dict[str, Any] = {}

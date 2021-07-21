# coding: utf-8

from enum import Enum, unique
from typing import Optional

from .base import BaseSettings
from .development import settings as dev_settings
from .production import settings as pro_settings


@unique
class EnvEnum(Enum):
    """环境枚举类"""
    DEV: BaseSettings = dev_settings
    PRO: BaseSettings = pro_settings


def get_settings(env: Optional[str] = None) -> BaseSettings:
    """获取配置"""
    
    if env is None:
        env = 'DEV'
    settings = getattr(EnvEnum, env.upper()).value
    return settings

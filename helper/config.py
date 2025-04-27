# coding: utf-8

from pydantic import Field

from util.pyd import ExtraIgnoreModel


class ServerConfig(ExtraIgnoreModel):

    debug: bool = Field(False)


class DatabaseConfig(ExtraIgnoreModel):

    user: str = Field("")
    password: str = Field("")
    host: str = Field("")
    port: int = Field(3306)
    database: str = Field("")


class RequestConfig(ExtraIgnoreModel):

    test_url: str = Field("", description="测试地址")


class Config(ExtraIgnoreModel):

    server: ServerConfig = Field(default_factory=ServerConfig, description="服务配置")
    db: DatabaseConfig = Field(default_factory=DatabaseConfig, description="数据库配置")
    request: RequestConfig = Field(default_factory=RequestConfig, description="请求配置")
    slow_timeout: float = Field(1.0, description="慢请求阈值")

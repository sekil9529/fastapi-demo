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

    server: ServerConfig
    db: DatabaseConfig
    request: RequestConfig

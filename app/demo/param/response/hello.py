# coding: utf-8

"""hello"""

from pydantic import Field
from pydantic.dataclasses import dataclass as pyd_dataclass


@pyd_dataclass
class Model:

    keyword: str = Field(..., title="关键字", example="hello world")

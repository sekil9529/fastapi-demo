from typing import Any

from pydantic import BaseModel

from core.response import ResponseModel


def res_model_factory(model: type[BaseModel], name: str = "") -> type[ResponseModel]:
    """响应模型工厂

    :param model: 模型
    :param name: 新模型名称
    :return: 新模型
    """
    if not name:
        name = f"_{model.__name__}__{ResponseModel.__name__}"
    dict_: dict[str, dict] = {
        "__annotations__": {"data": model},
    }
    new_model: type[ResponseModel] = type(name, (ResponseModel,), dict_)
    return new_model

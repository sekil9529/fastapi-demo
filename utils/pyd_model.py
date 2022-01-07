from pydantic import BaseModel

from core.response import ResponseModel

# 响应模型映射
RES_MODEL_MAP: dict[int, type[ResponseModel]] = {}


def res_model_factory(model: type[BaseModel], name: str = "") -> type[ResponseModel]:
    """响应模型工厂

    :param model: 模型
    :param name: 新模型名称
    :return: 新模型
    """
    model_id: int = id(model)
    global RES_MODEL_MAP
    if model_id not in RES_MODEL_MAP:
        if not name:
            name = f"_{model.__name__}__{model_id}__{ResponseModel.__name__}"
        dict_: dict[str, dict] = {
            "__annotations__": {"data": model},
        }
        new_model: type[ResponseModel] = type(name, (ResponseModel,), dict_)
        RES_MODEL_MAP[model_id] = new_model
    return RES_MODEL_MAP[model_id]


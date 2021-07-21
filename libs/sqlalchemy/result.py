# coding: utf-8

from typing import Union, List
from sqlalchemy.engine.row import Row
from sqlalchemy.orm.decl_api import DeclarativeMeta
try:
    from flask_sqlalchemy.model import Model
except ImportError:
    Model = DeclarativeMeta


from libs.dict import ExtDict


def model_format(model: Union[DeclarativeMeta, Model]) -> dict:
    """ 模型数据格式化 """
    return ExtDict((c.name, getattr(model, c.name, None)) for c in model.__table__.columns)


def row_format(result: Row) -> dict:
    """ 行数据格式化 """
    return ExtDict(zip(result.keys(), result))


def list_format(result: List[Union[Row, DeclarativeMeta, Model]]) -> List[dict]:
    """ 行数据列表格式化 """
    lst = []
    for items in result:
        if isinstance(items, Row):
            elem = row_format(items)
        elif isinstance(items, (DeclarativeMeta, Model)):
            elem = model_format(items)
        lst.append(elem)
    return lst


def result_format(result: Union[DeclarativeMeta, Model, Row, List, None]) -> Union[dict, List[dict]]:
    """ sqlalchemy query result 格式化 """
    if not result:
        return result
    elif isinstance(result, list):
        return list_format(result)
    elif isinstance(result, Row):
        return row_format(result)
    return model_format(result)

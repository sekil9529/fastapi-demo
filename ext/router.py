# coding: utf-8

from typing import Callable, Tuple, Union, List
from fastapi import APIRouter

router = APIRouter()
router.add_api_route()

class UrlPath:

    __slots__ = ('_params', '_kwargs')

    def __init__(self, path: str,
                 # name: str,
                 methods: Union[Tuple[str], List[str]],
                 endpoint: Callable,
                 **kwargs):
        self._params = {
            'path': path,
            # 'name': name,
            'methods': methods,
            'endpoint': endpoint,
        }
        self._params.update(kwargs)

    @property
    def params(self):
        return self._params

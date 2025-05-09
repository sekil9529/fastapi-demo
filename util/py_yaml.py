# coding: utf-8


import typing as t

import yaml


class PyYaml:
    """yaml配置类"""

    __slots__ = (
        "_yaml_str",
    )

    def __init__(self, path: str, encoding: str = "utf-8"):

        with open(path, "r", encoding=encoding) as f:
            yaml_str = f.read()
        self._yaml_str = yaml_str

    def to_dict(self) -> dict[str, t.Any]:

        return yaml.load(self._yaml_str, Loader=yaml.FullLoader)

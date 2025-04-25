# coding: utf-8

import typing as t


class DataclassProtocol(t.Protocol):
    """数据类"""

    __dataclass_fields__: t.ClassVar[t.Dict]
    # __dataclass_params__: t.ClassVar[t.Dict]
    # __post_init__: t.ClassVar[t.Callable[..., None]]

    def __init__(self, *args: object, **kwargs: object):

        pass

from configparser import RawConfigParser


class Environ(dict):
    """环境（只读）"""

    def __readonly__(self, *args, **kwargs):
        raise RuntimeError("Cannot modify ReadOnlyDict")

    def __getattr__(self, item):
        if item not in self:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")
        return self.__getitem__(item)

    __setattr__ = __readonly__
    __delattr__ = __readonly__
    __setitem__ = __readonly__
    __delitem__ = __readonly__
    pop = __readonly__
    popitem = __readonly__
    clear = __readonly__
    update = __readonly__
    setdefault = __readonly__
    del __readonly__


class Config:
    """配置文件"""

    __slots__ = ("_cp", "_config")

    def __init__(self, file: str, encoding: str = "utf-8"):
        self._cp: RawConfigParser = RawConfigParser()
        self._cp.read(file, encoding=encoding)
        self._config: dict[str, Environ] = {key: Environ(self._cp.items(key)) for key in self._cp.sections()}

    def __getattr__(self, block_name):
        """获取区块下的环境"""

        return self._config[block_name]

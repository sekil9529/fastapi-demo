# coding: utf-8

from pydantic import BaseModel
from pydantic.config import ConfigDict


EXTRA_IGNORE_CONFIG = ConfigDict(
    extra="ignore", validate_assignment=True, arbitrary_types_allowed=True, coerce_numbers_to_str=True)
EXTRA_ALLOW_CONFIG = ConfigDict(
    extra="allow", validate_assignment=True, arbitrary_types_allowed=True, coerce_numbers_to_str=True)


class ExtraAllowModel(BaseModel):

    model_config = EXTRA_ALLOW_CONFIG


class ExtraIgnoreModel(BaseModel):

    model_config = EXTRA_IGNORE_CONFIG

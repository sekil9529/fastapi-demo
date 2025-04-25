# coding: utf-8

import calendar
from datetime import datetime, timedelta, date


def from_unix_timestamp(secs: float | int) -> datetime:
    """时间戳转datetime"""
    try:
        dt = datetime.fromtimestamp(secs)
    except OSError:  # 兼容windows环境
        dt = datetime(1970, 1, 1, 8) + timedelta(seconds=secs)
    return dt


def to_unix_timestamp(dt: datetime | date) -> int:
    """datetime转时间戳"""

    if isinstance(dt, date):
        dt = datetime(dt.year, dt.month, dt.day)
    try:
        secs = int(dt.timestamp())
    except OSError:  # 兼容windows环境
        # 只能保留到整数位
        secs = calendar.timegm((dt + timedelta(hours=-8)).timetuple())
    return secs

# -*- coding:utf-8 -*-

import time
import datetime


def get_cur_timestamp():
    """ 获取当前时间戳
    """
    ts = int(time.time())
    return ts


def ts_to_datetime(ts):
    """ 将时间戳转换为datetime类型
    @param ts 时间戳
    """
    if not ts:
        return '00-00-00 00:00:00'
    dt = datetime.datetime.utcfromtimestamp(int(ts)) + datetime.timedelta(hours=8)
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def datetime_to_display(dt):
    """ """
    if not dt:
        return '00-00-00 00:00:00'
    if not isinstance(dt, datetime.datetime):
        return '00-00-00 00:00:00'

    return dt.strftime("%Y-%m-%d %H:%M:%S")

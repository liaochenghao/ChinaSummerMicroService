# -*- coding: utf-8 -*-
from core.error import ValidationError
from utils import datetime_help


def _field(data, field=None, required=True):
    data = {} if data is None else data
    field_data = data.get(field) if field else data

    if required and field_data is None:
        raise ValidationError('参数错误, %s为必填参数' % field)
    if data is None:
        return None
    return field_data


def bool_field(data, field=None, required=True):
    field_data = _field(data, field, required)
    if str(field_data).lower() == 'true':
        return True
    if str(field_data).lower() == 'false':
        return False
    raise ValidationError('参数错误, %s需要是bool类型' % field)


def int_field(data, field=None, required=True):
    field_data = _field(data, field, required)
    try:
        return int(field_data) if (field_data is not None) else None
    except:
        raise ValidationError('参数错误, %s需要是int类型' % field)


def float_field(data, field=None, required=True):
    field_data = _field(data, field, required)
    try:
        return float(field_data) if (field_data is not None) else None
    except:
        raise ValidationError('参数错误, %s需要是float类型' % field)


def char_field(data, field=None, required=True):
    field_data = _field(data, field, required)
    return str(field_data) if (field_data is not None) else None


def datetime_field(data, field=None, required=True):
    field_data = _field(data, field, required)
    try:
        return datetime_help.parse_datetime(field_data) if (field_data is not None) else None
    except:
        raise ValidationError('参数错误, %s需要是ISO_8601格式的时间字符串' % field)


def date_field(data, field=None, required=True):
    field_data = _field(data, field, required)
    try:
        return datetime_help.parse_date(field_data) if (field_data is not None) else None
    except:
        raise ValidationError('参数错误, %s需要是ISO_8601格式的日期字符串' % field)


def list_field(data, field=None, required=True):
    field_data = _field(data, field, required)
    if field_data is None:
        return None
    if not isinstance(field_data, list):
        raise ValidationError('参数错误, %s需要是list类型' % field)
    return field_data


def dict_field(data, field=None, required=True):
    field_data = _field(data, field, required)
    if field_data is None:
        return None
    if not isinstance(field_data, dict):
        raise ValidationError('参数错误, %s需要是dict类型' % field)
    return field_data


class BaseValidator:
    field_map = (
        ('int', int_field),
        ('char', char_field),
        ('float', float_field),
        ('date', date_field),
        ('datetime', datetime_field),
        ('list', list_field),
        ('dict', dict_field),
        ('bool', bool_field)
    )

    def __init__(self, validate_data, server_type='stu_system'):
        self.validate_data = validate_data
        self.server_type = server_type

    def validate(self):
        pass

    def validate_func(self, field_type, field_name, validate_data):

        valid_func = dict(self.field_map).get(field_type)
        return valid_func(data=validate_data, field=field_name)
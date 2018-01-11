# coding: utf-8
from core.validators import char_field, int_field, float_field, date_field, datetime_field, list_field, dict_field, bool_field


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

    def validate_func(self, field_type, field_name, validate_data):

        valid_func = dict(self.field_map).get(field_type)
        return valid_func(data=validate_data, field=field_name)


class AuthorizeValidator(BaseValidator):

    def __init__(self, validate_data):
        self.validate_data = validate_data

    def validate(self):
        self.validate_func('char', 'ticket', self.validate_data)
        return self.validate_data
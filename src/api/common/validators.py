# coding: utf-8
from core.validators import BaseValidator
from core.error import ValidationError


class TicketAuthorizeValidator(BaseValidator):

    def validate(self):
        self.validate_func('char', 'ticket', self.validate_data)
        return self.validate_data


class UserAuthorizeValidator(BaseValidator):

    def validate(self):
        if not self.validate_data.get('user_id'):
            raise ValidationError('user_id不能为空')
        return self.validate_data
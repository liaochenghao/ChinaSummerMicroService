# coding: utf-8
from core.validators import BaseValidator


class TicketAuthorizeValidator(BaseValidator):

    def validate(self):
        self.validate_func('char', 'ticket', self.validate_data)
        return self.validate_data


class UserAuthorizeValidator(BaseValidator):
    def validate(self):
        self.validate_func('int', 'user_id', self.validate_data)
        return self.validate_data
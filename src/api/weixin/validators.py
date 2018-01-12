# coding: utf-8
from core.validators import BaseValidator


class TextMessageValidator(BaseValidator):

    def validate(self):
        self.validate_func('char', 'openid', self.validate_data)
        self.validate_func('char', 'content', self.validate_data)
        return self.validate_data


class TemplateMessageValidator(BaseValidator):

    def validate(self):
        self.validate_func('char', 'openid', self.validate_data)
        self.validate_func('char', 'template_id', self.validate_data)
        self.validate_func('dict', 'send_data', self.validate_data)


class UserInfoValidator(BaseValidator):
    def validate(self):
        self.validate_func('char', 'openid', self.validate_data)

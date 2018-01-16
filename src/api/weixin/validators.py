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
        return self.validate_data


class UserInfoValidator(BaseValidator):
    def validate(self):
        self.validate_func('char', 'openid', self.validate_data)
        return self.validate_data


class TemporaryQrCodeValidator(BaseValidator):
    def validate(self):
        self.validate_func('char', 'action_name', self.validate_data)
        self.validate_func('int', 'expired_seconds', self.validate_data)
        return self.validate_data


class ForeverQrCodeValidator(BaseValidator):
    def validate(self):
        self.validate_func('char', 'action_name', self.validate_data)
        return self.validate_data
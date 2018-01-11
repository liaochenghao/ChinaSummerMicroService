# coding: utf-8

from core.routes import route
# from utils import log as logger
from core.webbase import WebHandler
from api.stu_system.validators import AuthorizeValidator


@route(r'/api/stu_system/auth/authorize/$')
class StuSystemAuthorizeHandler(WebHandler):
    """学生系统验证"""

    def get(self, *args, **kwargs):
        data = {'ticket': 'a'}
        validator = AuthorizeValidator(**data)
        validated_data = validator.validate_data()
        ticket = validated_data['ticket']
        self.write(data)

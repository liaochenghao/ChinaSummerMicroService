# coding: utf-8

from core.routes import route
# from utils import log as logger
from core.webbase import WebHandler
from api.stu_system.validators import AuthorizeValidator
from service.stu_system.functions import StuSystemAuthorize


@route(r'/api/stu_system/auth/authorize/$')
class StuSystemAuthorizeHandler(WebHandler):
    """学生系统验证"""

    def get(self, *args, **kwargs):
        ticket = self.get_param('ticket')
        validator = AuthorizeValidator({'ticket': ticket})
        validated_data = validator.validate()
        ticket = validated_data['ticket']
        res = StuSystemAuthorize.validate_ticket(ticket)
        self.do_success(res)

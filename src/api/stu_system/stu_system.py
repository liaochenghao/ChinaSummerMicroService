# coding: utf-8

from core.routes import route
# from utils import log as logger
from core.webbase import WebHandler
from api.stu_system.validators import TicketAuthorizeValidator, UserAuthorizeValidator
from service.stu_system.functions import StuSystemAuthorize


@route(r'/api/stu_system/auth/authorize/$')
class StuSystemAuthorizeHandler(WebHandler):
    """学生系统验证"""

    def get(self, *args, **kwargs):
        ticket = self.get_param('ticket')
        validator = TicketAuthorizeValidator({'ticket': ticket})
        validated_data = validator.validate()
        ticket = validated_data['ticket']
        res = StuSystemAuthorize.validate_ticket(ticket)
        self.do_success(res)

    def post(self, *args, **kwargs):
        data = self.data
        validator = UserAuthorizeValidator(data)
        validated_data = validator.validate()
        res = StuSystemAuthorize.create_ticket(validated_data['user_id'])
        self.do_success(res)

    def delete(self, *args, **kwargs):
        ticket = self.get_param('ticket')
        validator = TicketAuthorizeValidator({'ticket': ticket})
        validated_data = validator.validate()
        ticket = validated_data['ticket']
        StuSystemAuthorize.delete_ticket(ticket)
        self.do_success()


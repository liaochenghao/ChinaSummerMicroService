# coding: utf-8

from core.routes import route
from core.webbase import WebHandler
from api.common.validators import TicketAuthorizeValidator, UserAuthorizeValidator
from service.stu_system.functions import StuSystemAuthorize


@route(r'/api/common/auth/authorize/$')
class CommonAuthorizeHandler(WebHandler):
    """学生系统验证"""

    def get(self, *args, **kwargs):
        ticket = self.get_param('ticket')
        server_type = self.get_param('server_type', 'stu_system')
        validator = TicketAuthorizeValidator({'ticket': ticket}, server_type)
        validated_data = validator.validate()
        ticket = validated_data['ticket']
        res = StuSystemAuthorize.validate_ticket(ticket, server_type=server_type)
        self.do_success(res)

    def post(self, *args, **kwargs):
        data = self.data
        server_type = self.get_param('server_type', 'stu_system')
        validator = UserAuthorizeValidator(data)
        validated_data = validator.validate()
        res = StuSystemAuthorize.create_ticket(validated_data['user_id'], server_type)
        self.do_success(res)

    def delete(self, *args, **kwargs):
        ticket = self.get_param('ticket')
        server_type = self.get_param('server_type', 'stu_system')
        validator = TicketAuthorizeValidator({'ticket': ticket}, server_type)
        validated_data = validator.validate()
        ticket = validated_data['ticket']
        StuSystemAuthorize.delete_ticket(ticket, server_type)
        self.do_success()


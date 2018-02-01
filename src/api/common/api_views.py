# coding: utf-8
from core.routes import route
from core.webbase import WebHandler
from api.common.validators import TicketAuthorizeValidator, UserAuthorizeValidator
from service.stu_system.functions import StuSystemAuthorize


@route(r'/api/common/auth/authorize/$')
class CommonAuthorizeHandler(WebHandler):
    """学生系统验证"""

    async def get(self, *args, **kwargs):
        ticket = self.get_param('ticket')
        validator = TicketAuthorizeValidator({'ticket': ticket})
        validated_data = validator.validate()
        ticket = validated_data['ticket']
        res = await StuSystemAuthorize.validate_ticket(ticket)
        self.do_success(res)

    async def post(self, *args, **kwargs):
        data = self.data
        validator = UserAuthorizeValidator(data)
        validated_data = validator.validate()
        res = await StuSystemAuthorize.create_ticket(validated_data['user_id'])
        self.do_success(res)

    async def delete(self, *args, **kwargs):
        ticket = self.get_param('ticket')
        validator = TicketAuthorizeValidator({'ticket': ticket})
        validated_data = validator.validate()
        ticket = validated_data['ticket']
        await StuSystemAuthorize.delete_ticket(ticket)
        self.do_success()


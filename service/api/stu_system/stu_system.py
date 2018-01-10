# coding: utf-8

# from simpleroute import route
from core.routes import route
from utils import log as logger
from core.webbase import WebHandler


@route(r'/api/stu_system/auth/authorize/$')
class StuSystemAuthorizeHandler(WebHandler):
    """学生系统验证"""

    def get(self, *args, **kwargs):
        data = {'code': 'msg'}
        self.write(data)

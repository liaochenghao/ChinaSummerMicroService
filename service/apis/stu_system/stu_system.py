# coding: utf-8

from simpleroute import route
from utils import log as logger
from core.webbase import WebHandler


@route(r'/api/stu_system/authorize/$')
class StuSystemAuthorize(WebHandler):
    """学生系统验证"""

    def post(self, *args, **kwargs):

        self.write()

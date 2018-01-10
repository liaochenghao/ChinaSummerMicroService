# -*- coding:utf-8 -*-

""" 全局系统变量、对象
"""

import os

from tornado.options import options

# tornado
from simpleroute import make_routes

import config
from utils import log as logger


class MicroContext(object):
    """  全局系统变量、对象
    """

    def __init__(self):
        """ 初始化
        """
        src_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        root_dir = os.path.dirname(src_dir)

        self.src_dir = src_dir
        self.root_dir = root_dir

        # 初始化日志
        if config.RUN_MODE == 'console':
            logger.initLogger()
        else:
            logfile = '%s_%s.log' % (config.LOG_CONFIG['filename'].split('.')[0], 7070)
            logger.initLogger(config.LOG_CONFIG['level'], config.LOG_CONFIG['path'], logfile)
        options.parse_command_line()

        # 初始化数据库对象
        self.init_db_instance()

    def init_uri_routes(self):
        """ 初始化uri路由
        """
        logger.info('init uri routes start >>>', caller=self)
        handlers = make_routes(['apis'])
        for item in handlers:
            logger.info('uri:', item[0], 'handler:', item[1], caller=self)
        self.handlers = handlers
        logger.info('init uri routes done <<<', caller=self)

    def init_db_instance(self):
        """ 初始化数据库对象
        """
        logger.info('init db instance start >>>', caller=self)

        from core.db.mysql import initMySQL
        initMySQL(**config.MYSQL_CONFIG)

        logger.info('init db instance done <<<', caller=self)


Context = MicroContext()

__all__ = [Context]

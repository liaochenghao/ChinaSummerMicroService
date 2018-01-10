# coding: utf-8
"""
auth: qiulei
email: 896275756@qq.com
date: 2018-01-10
"""

import tornado
import tornado.web
import tornado.httpserver
import tornado.ioloop
import sys
import config
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado import options
from core.context import TornadoContext
from utils import log as logger


class Application(tornado.web.Application):
    """ app 入口
    """

    def __init__(self, handlers):
        """ 初始化"""
        settings = {
            'debug': True,
            'cookie_secret': 'fd49713d91e0e863a88740432af6644b123'
        }
        tornado.web.Application.__init__(self, handlers, **settings)
        logger.info('init app done.', caller=self)


def main(http_port):
    configs = {
        'run_mode': config.RUN_MODE,
        'log_level': config.LOG_CONFIG.get('level'),
        'log_path': config.LOG_CONFIG.get('path'),
        'log_name': config.LOG_CONFIG.get('filename'),
        'mysql_config': config.MYSQL_CONFIG,
        'handler_pathes': ['api'],
        'http_port': http_port,
    }
    t_context = TornadoContext(**configs)
    http_server = tornado.httpserver.HTTPServer(Application(t_context.handlers))
    http_server.listen(http_port)
    logger.info('listen http port at:', http_port)

    logger.info('start io loop ...')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    port = 7070
    if len(sys.argv) > 1:
        port = sys.argv[1]
    main(port)
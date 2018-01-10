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

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado import options
from utils import log as logger


class Application(tornado.web.Application):
    """ app 入口
    """

    def __init__(self):
        """ 初始化
        """
        from core.context import KLCContext
        KLCContext.init_uri_routes()
        settings = {
            'debug': True,
            'cookie_secret': 'fd49713d91e0e863a88740432af6644b'
        }
        tornado.web.Application.__init__(self, KLCContext.handlers, **settings)
        logger.info('init app done.', caller=self)


def main(http_port):
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    logger.info('listen http port at:', options.port)

    logger.info('start io loop ...')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    port = 7002
    if len(sys.argv) > 1:
        port = sys.argv[1]
    main(port)
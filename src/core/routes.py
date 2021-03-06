# -*- coding:utf-8 -*-

"""
http uri 路由装饰器
Date:   2017/09/20
"""


class route(object):
    """
    @route('/some/path')
    class SomeRequestHandler(RequestHandler):
        pass
    @route('/some/path', name='other')
    class SomeOtherRequestHandler(RequestHandler):
        pass
    my_routes = route.make_routes(['api'])
    """

    _routes = []

    def __init__(self, uri, name=None):
        """ 装饰器
        @param uri 注册的uri名字，支持uri正则表达式
        @param name 注册的uri别名
        """
        self.uri = uri
        if not name:
            name = '-'.join(uri.split('/'))
        self.name = name

    def __call__(self, _handler):
        """ gets called when we class decorate
        """
        self._routes.append({'uri': self.uri, 'name': self.name, 'handler': _handler})
        return _handler

    @classmethod
    def make_routes(cls, dirs):
        """ 注册并返回所有的handler
        @param dirs list，需要注册uri路由的处理方法路径
        """
        for dir in dirs:
            s = 'import %s' % dir
            exec(s)
        routes = []
        for handler_dic in cls._routes:
            routes.append((handler_dic.get('uri'), handler_dic.get('handler')))
        return routes

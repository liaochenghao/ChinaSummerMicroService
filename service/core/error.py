# -*- coding:utf-8 -*-

""" 定义一些错误类型，在出现的时候抛出异常
"""


class CustomError(Exception):
    """ 通用类型错误
    """

    def __init__(self, err_msg='', err_code=1):
        super(CustomError, self).__init__()
        self.err_code = err_code
        self.err_msg = err_msg


class ParamsError(Exception):
    """ http请求参数错误
    """

    def __init__(self, err_msg='参数错误', err_code=1):
        super(ParamsError, self).__init__()
        self.err_code = err_code
        self.err_msg = err_msg


class SystemError(Exception):
    """ 系统内部错误
    """

    def __init__(self, err_msg='SYSTEM ERRROR', http_code=500):
        super(SystemError, self).__init__()
        self.http_code = http_code
        self.err_msg = err_msg


class ApiError(Exception):
    """ API使用错误
    """

    def __init__(self, err_msg='NOT FOUND', http_code=404):
        super(ApiError, self).__init__()
        self.http_code = http_code
        self.err_msg = err_msg


class SessionError(Exception):
    """ session错误，需要用户重新登陆授权
    """

    def __init__(self, err_msg='AUTH ERROR', http_code=403):
        super(SessionError, self).__init__()
        self.http_code = http_code
        self.err_msg = err_msg

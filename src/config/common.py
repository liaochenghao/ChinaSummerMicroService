# coding: utf-8
# 运行模式 online为线上服务器，inner-test为内测测试服，test为测试服，console为本地调试
# online/inner-test/test模式将会把日志写入日志文件，console模式不写日志文件而打印到控制台
import os

RUN_MODE = 'online'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 署校联盟服务中心微信公众号配置
WX_CONFIG = {
    'APP_ID': 'wx6cdbbafe0da85703',
    'APP_SECRET': '73c8e307c09027162840705e7496ed32'
}

# 日志文件
LOG_CONFIG = {
    'level': 'debug',   # 日志级别 info debug
    'path': '%s/logs' % BASE_DIR,   # 日志保存路径
    'filename': 'debug.log'  # 日志保存名字，名字后缀会自动加上进程监听http端口号
}
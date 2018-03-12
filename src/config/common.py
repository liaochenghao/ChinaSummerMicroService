# coding: utf-8
# 运行模式 online为线上服务器，inner-test为内测测试服，test为测试服，console为本地调试
# online/inner-test/test模式将会把日志写入日志文件，console模式不写日志文件而打印到控制台
import os

RUN_MODE = 'online'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 北美留学生社区微信公众号配置
WX_CONFIG = {
    'APP_ID': 'wxddf82dc1f4c6b5e0',
    'APP_SECRET': '10410cf627a6a114d9bc6ed466bed242'
}

# 日志文件
LOG_CONFIG = {
    'level': 'debug',   # 日志级别 info debug
    'path': '%s/logs' % BASE_DIR,   # 日志保存路径
    'filename': 'debug.log'  # 日志保存名字，名字后缀会自动加上进程监听http端口号
}
# coding: utf-8
from config.common import *
import pymysql

RUN_MODE = 'console'

MYSQL_CONFIG = {
    'host': '120.79.36.26',
    'port': 3306,
    'db': 'stu_system',
    'user': 'root',
    'password': '1q2w3e4r!Q',
    'cursorclass': pymysql.cursors.DictCursor,
    'charset': 'utf8'
}


REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379
}
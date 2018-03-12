# coding: utf-8
from config.common import *
import pymysql

RUN_MODE = 'console'

MYSQL_CONFIG = {
    'host': '47.92.115.126',
    'port': 3306,
    'db': 'stu_system',
    'user': 'root',
    'password': 'svLE26eg',
    'cursorclass': pymysql.cursors.DictCursor,
    'charset': 'utf8'
}


REDIS_CONFIG = {
    'host': '47.92.115.126',
    'port': 6379
}
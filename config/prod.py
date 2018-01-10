import pymysql

# 署校联盟服务中心微信公众号配置
WX_CONFIG = {
    'APP_ID': 'wx6cdbbafe0da85703',
    'APP_SECRET': '73c8e307c09027162840705e7496ed32'
}

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
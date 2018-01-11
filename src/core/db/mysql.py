# -*- coding:utf-8 -*-

from tornado_mysql import pools, cursors
from utils import log as logger

pools.DEBUG = True
CONN_POOL = None


def initMySQL(host='127.0.0.1', port=3306, user='root', password='', db='mysql'):
    """ 初始化mysql连接池
    """
    mysql_config = {
        'host': host,
        'port': port,
        'user': user,
        'passwd': password,
        'db': db,
        'cursorclass': cursors.DictCursor,
        'charset': 'utf8'
    }
    logger.info('mysql_config:', mysql_config)
    global CONN_POOL
    CONN_POOL = pools.Pool(mysql_config,
                           max_idle_connections=1,
                           max_recycle_sec=3)
    logger.info('create mysql connection pool.')


async def exec_cmd(sql):
    """ 执行mysql命令
    @param sql sql命令
    """
    sql = sql.replace('\t', ' ').replace('\n', ' ')
    logger.debug('sql:', sql)
    cursor = await CONN_POOL.execute(sql)
    result = cursor.fetchall()
    return result


__all__ = [initMySQL, exec_cmd]

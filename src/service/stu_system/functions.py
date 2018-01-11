# coding: utf-8
import datetime

from core.db.mysql import my_custom_sql
from core.db.redis_server import redis_client


class StuSystemAuthorize:

    @staticmethod
    def validate_ticket(ticket):
        cached_ticket = redis_client.get_instance('ticket')
        if cached_ticket:
            valid_ticket = True
            user_id = cached_ticket
            err_msg = None
        else:
            sql = """
                select * from ticket where ticket="%s"
            """ % ticket
            res_ticket = my_custom_sql(sql)
            if not res_ticket:
                valid_ticket = False
                user_id = None
                err_msg = 'ticket不存在'
            else:
                ticket = res_ticket[0]
                if ticket['expired_time'] > datetime.datetime.now():
                    valid_ticket = True
                    user_id = ticket['user_id']
                    err_msg = None
                    redis_client.set_instance(ticket, user_id)
                else:
                    valid_ticket = False
                    user_id = None
                    err_msg = 'ticket已过期'
        return {'valid_ticket': valid_ticket, 'user_id': user_id, 'err_msg': err_msg}
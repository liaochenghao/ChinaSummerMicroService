# coding: utf-8
import datetime
import random
import string

from core.db.redis_server import redis_client
from core.db.mysql_pool import mysql


class StuSystemAuthorize:

    @staticmethod
    async def validate_ticket(ticket, server_type='stu_system'):
        cached_user_id = redis_client.get_instance(ticket)
        if cached_user_id:
            valid_ticket = True
            user_id = cached_user_id
            err_msg = None
        else:
            if server_type == 'stu_system':
                sql = """
                    select * from ticket where ticket="%s"
                """ % ticket
            elif server_type == 'ugc_system':
                sql = """
                    select * from smart_programs.authentication_ticket where ticket="%s"
                """ % ticket
            else:
                pass
            res_ticket = await mysql.getOne(sql)
            if not res_ticket:
                valid_ticket = False
                user_id = None
                err_msg = 'ticket不存在'
            else:
                ticket = res_ticket
                if ticket['expired_time'] > datetime.datetime.now():
                    valid_ticket = True
                    user_id = ticket['user_id']
                    err_msg = None
                    redis_client.set_instance(key=ticket['ticket'], value=user_id)
                else:
                    valid_ticket = False
                    user_id = None
                    err_msg = 'ticket已过期'
        return {'valid_ticket': valid_ticket, 'user_id': user_id, 'err_msg': err_msg}

    @staticmethod
    async def create_ticket(user_id, server_type='stu_system'):
        now = datetime.datetime.now()
        expired_time = datetime.datetime.now() + datetime.timedelta(days=1)
        ticket = 'TK-'
        ticket += ''.join(random.sample(string.digits + string.ascii_letters, 20))
        if server_type == 'stu_system':
            sql = """
                insert into ticket (user_id, create_time, expired_time, ticket) values(%d, "%s", "%s", "%s")        
            """ % (user_id, str(now), str(expired_time), ticket)
        elif server_type == 'ugc_system':
            sql = """
                    insert into smart_programs.authentication_ticket (user_id, create_time, expired_time, ticket) values(%d, "%s", "%s", "%s")        
            """ % (user_id, str(now), str(expired_time), ticket)
        else:
            pass
        await mysql.insertOne(sql)
        await mysql.end()
        redis_client.set_instance(ticket, user_id)
        return {'ticket': ticket}

    @staticmethod
    async def delete_ticket(ticket, server_type='stu_system'):
        if server_type == 'stu_system':
            sql = """
                delete from ticket where ticket="%s"    
            """ % ticket
        elif server_type == 'ugc_system':
            sql = """
                delete from smart_programs.authentication_ticket where ticket="%s"
            """ % ticket
        redis_client.delete(ticket)
        await mysql.delete(sql)
        await mysql.end()
        return
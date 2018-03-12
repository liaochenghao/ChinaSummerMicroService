# coding: utf-8
from secrets import token_hex
from core.db.redis_server import redis_client
from utils import log as logger


class StuSystemAuthorize:
    @staticmethod
    async def validate_ticket(ticket):
        logger.info('Student System Validate Ticket')
        cached_user_id = redis_client.get_instance(ticket)
        logger.info('Get Cached User Id: %s' % cached_user_id)
        if cached_user_id:
            valid_ticket = True
            user_id = cached_user_id
            err_msg = None
        else:
            valid_ticket = False
            user_id = None
            err_msg = 'ticket不存在'
        return {'valid_ticket': valid_ticket, 'user_id': user_id, 'err_msg': err_msg}

    @staticmethod
    async def create_ticket(user_id):
        ticket = token_hex(32)
        redis_client.set_instance(ticket, user_id)
        return {'ticket': ticket}

    @staticmethod
    async def delete_ticket(ticket):
        redis_client.delete(ticket)
        return

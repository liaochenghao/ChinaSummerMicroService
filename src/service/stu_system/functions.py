# coding: utf-8
from core.db.mysql import exec_cmd


class StuSystemAuthorize:

    @staticmethod
    def validate_ticket(ticket):
        sql = """
            select * from ticket
        """
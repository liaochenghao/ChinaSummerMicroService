# coding: utf-8
import json
import requests
from config import WX_CONFIG

from core.db.redis_server import redis_client


class WeiXinClient:

    def __init__(self):
        self.APP_ID = WX_CONFIG['APP_ID']
        self.APP_SECRET = WX_CONFIG['APP_SECRET']

    def get(self, url, params):
        res = requests.get(url, params).json()
        if res.get('errcode', 0) != 0:
            redis_client.delete('server_center_access_token')
            res = requests.get(url, params).json()
        return res

    def post(self, url, json_data):
        res = requests.post(url, json=json_data).json()
        if res.get('errcode', 0) != 0:
            redis_client.delete('server_center_access_token')
            res = requests.post(url, json=json_data).json()
        return res

    @property
    def get_valid_access_token(self):
        cached_access_token = redis_client.get_instance('server_center_access_token')
        if not cached_access_token:
            cached_access_token = self.get_grant_token()
        print(cached_access_token)
        return cached_access_token

    def get_grant_token(self):
        """获取微信access_token"""
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
            self.APP_ID, self.APP_SECRET)
        res = requests.get(url)
        res_data = res.json()
        redis_client.set_instance('server_center_access_token', res_data['access_token'], default_valid_time=(2*60*60 - 100))
        return res_data['access_token']

    def send_text_message(self, openid, content, access_token=None):
        """发送文本消息"""
        url = "https://api.weixin.qq.com/cgi-bin/message/custom/send"
        if not access_token:
            access_token = self.get_valid_access_token
        querystring = {
            "access_token": access_token}

        payload = ("{\"touser\": \"%s\", \"msgtype\": \"text\",  \"text\": {\"content\": \"%s\" }}" % (openid, content)).encode('utf-8')
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "3a32082a-0052-5591-5a7e-bf815defb396"
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        return response.json()

    def template_send(self, openid, template_id, url, access_token=None, **kwargs):
        """
        发送模板消息
        """
        data = {}

        if not access_token:
            access_token = self.get_valid_access_token

        for key, value in kwargs.items():
            # 转换成微信要求格式
            data[key] = {
                'value': value,
                'color': '#173177'
            }
        post_data = {
            'touser': openid,
            'template_id': template_id,
            'url': url,
            'data': data
        }
        base_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % access_token

        res = self.post(url=base_url, json_data=post_data)
        return res

    def code_authorize(self, code):
        """用code获取认证"""
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token/'
        params = {
            'appid': self.APP_ID,
            'secret': self.APP_SECRET,
            'code': code,
            'grant_type': 'authorization_code'
        }
        res = self.get(url, params)
        return res

    def get_user_info(self, openid, access_token=None):
        """
        通过openid获取基础用户信息
        """
        if not access_token:
            access_token = self.get_valid_access_token
        url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN" % (access_token, openid)
        res = self.get(url, params={})
        return res

    def get_web_user_info(self, openid, access_token):
        """
        通过openid获取网页授权的用户信息
        """
        url = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN" % (access_token, openid)
        res = self.get(url, params={})
        return res


wx_client = WeiXinClient()
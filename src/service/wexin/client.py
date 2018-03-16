# coding: utf-8
import json

import requests
from config import WX_CONFIG

from core.db.redis_server import redis_client


class WeiXinClient:
    def __init__(self):
        self.APP_ID = WX_CONFIG['APP_ID']
        self.APP_SECRET = WX_CONFIG['APP_SECRET']

    async def get(self, url, params):
        res = requests.get(url, params).json()
        return res

    async def post(self, url, json_data):
        res = requests.post(url, json=json_data).json()
        return res

    async def get_valid_access_token(self, app_id=None, app_secret=None):
        print('kkkkkkkkkkkkkkkkkkkkkkkkkk')
        cached_token_app_id = app_id if app_id else self.APP_ID
        print('gggggggggggggggggggggggggg')
        cached_access_token = redis_client.get_instance('%s_access_token' % cached_token_app_id)
        print('ooooooooooooooooooooooo'+str(cached_access_token))
        if not cached_access_token:
            cached_access_token = await self.get_grant_token(app_id, app_secret)
            print('mmmmmmmmmmmmmmmmmmmmm' + str(cached_access_token))
            redis_client.set_instance('%s_access_token' % cached_token_app_id, cached_access_token)
        return cached_access_token

    async def get_grant_token(self, app_id, app_secret):
        """获取微信access_token"""
        app_id = app_id if app_id else self.APP_ID
        app_secret = app_secret if app_secret else self.APP_SECRET
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
            app_id, app_secret)
        res = requests.get(url)
        res_data = res.json()
        redis_client.set_instance('%s_access_token' % app_id, res_data['access_token'],
                                  default_valid_time=(2 * 60 * 60 - 100))
        return res_data['access_token']

    async def send_text_message(self, openid, content, access_token=None):
        """发送文本消息"""
        url = "https://api.weixin.qq.com/cgi-bin/message/custom/send"
        if not access_token:
            access_token = self.get_valid_access_token()
        querystring = {
            "access_token": access_token}

        payload = (
        "{\"touser\": \"%s\", \"msgtype\": \"text\",  \"text\": {\"content\": \"%s\" }}" % (openid, content)).encode(
            'utf-8')
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "3a32082a-0052-5591-5a7e-bf815defb396"
        }

        response = await requests.request("POST", url, data=payload, headers=headers, params=querystring)
        return response.json()

    async def template_send(self, openid, template_id, url, access_token=None, **kwargs):
        """
        发送模板消息
        """
        data = {}

        if not access_token:
            access_token = self.get_valid_access_token()

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

        res = await self.post(url=base_url, json_data=post_data)
        return res

    async def code_authorize(self, code, app_id=None, app_secret=None):
        """用code获取认证"""
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token'
        app_id = app_id if app_id else self.APP_ID
        app_secret = app_secret if app_secret else self.APP_SECRET
        params = {
            'appid': app_id,
            'secret': app_secret,
            'code': code,
            'grant_type': 'authorization_code'
        }
        res = await self.get(url, params)
        return res

    async def get_user_info(self, openid, access_token=None):
        """
        通过openid获取基础用户信息
        """
        if not access_token:
            access_token = self.get_valid_access_token()
        url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN" % (
        access_token, openid)
        res = await self.get(url, params={})
        return res

    async def get_web_user_info(self, openid, access_token=None):
        """
        通过openid获取网页授权的用户信息
        """
        if not access_token:
            access_token = self.get_valid_access_token()
        url = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN" % (access_token, openid)
        response = requests.get(url, params={})
        response.encoding = 'utf-8'
        return response.json()

    async def get_temporary_qr_code(self, action_name, scene_id, expired_seconds=7 * 24 * 60 * 60, access_token=None):
        """获取临时二维码"""
        if not access_token:
            access_token = self.get_valid_access_token()

        if action_name == 'QR_SCENE':
            scene_data = {'scene_id': scene_id}
        else:
            scene_data = {'scene_str': scene_id}
        url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % access_token
        json_data = {
            "expire_seconds": expired_seconds,
            "action_name": action_name,
            "action_info": {
                "scene": scene_data
            }
        }
        res = await self.post(url=url, json_data=json_data)
        res['qr_img_url'] = 'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s' % res['ticket']
        return res

    async def get_forever_qr_code(self, action_name, scene_id, access_token):
        """获取永久二维码"""
        if not access_token:
            access_token = self.get_valid_access_token()
            print(':hhhhhhhhhhhhhhhhh:access_token %s' % str(access_token))
        if action_name == 'QR_LIMIT_SCENE':
            scene_data = {'scene_id': scene_id}
        else:
            scene_data = {'scene_str': scene_id}
        url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % access_token
        json_data = {
            "action_name": action_name,
            "action_info": {
                "scene": scene_data
            }
        }
        res = await self.post(url=url, json_data=json_data)
        res['qr_img_url'] = 'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s' % res['ticket']
        return res

    async def img_content_send(self, access_token, openid, articles):
        """
        发送图文消息
        :param access_token:
        :param openid:
        :param articles:  list 发送文本列表
        :return:
        """
        if not access_token:
            access_token = self.get_valid_access_token()
        url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s" % access_token
        data = {
            "touser": openid,
            "msgtype": "news",
            "news": {
                "articles": articles
            }
        }
        res = requests.post(url=url, data=json.dumps(data, ensure_ascii=False).encode('utf-8')).json()
        return res


wx_client = WeiXinClient()

# coding: utf-8
from core.routes import route
from core.webbase import WebHandler
from service.wexin.client import wx_client
from api.weixin.validators import TextMessageValidator, TemplateMessageValidator, UserInfoValidator, \
    TemporaryQrCodeValidator, ForeverQrCodeValidator


@route(r'/api/weixin/service_center/access_token/$')
class WeXinServerAccessToken(WebHandler):
    """
    微信服务access_token
    """

    async def get(self, *args, **kwargs):
        app_id = self.get_param('app_id')
        app_secret = self.get_param('app_secret')
        access_token = await wx_client.get_valid_access_token(app_id, app_secret)
        self.do_success({'access_token': access_token})


@route(r'/api/weixin/service_center/send_text_message/$')
class WeXinServerTextMessage(WebHandler):
    """
    通过客服消息接口，给用户发送文本消息
    """
    async def post(self, *args, **kwargs):
        openid = self.data.get('openid')
        content = self.data.get('content')
        access_token = self.data.get('access_token', None)

        validator = TextMessageValidator({'openid': openid, 'content': content})
        validator.validate()
        res = await wx_client.send_text_message(openid=openid, content=content, access_token=access_token)
        self.do_success(res)


@route(r'/api/weixin/service_center/send_template_message/$')
class WeiXinServerTemplateMessage(WebHandler):
    """
    发送模板消息
    """
    async def post(self, *args, **kwargs):
        template_id = self.data.get('template_id')
        openid = self.data.get('openid')
        send_data = self.data.get('send_data')
        url = self.data.get('url')
        access_token = self.data.get('access_token', None)

        validator = TemplateMessageValidator({'template_id': template_id, 'openid': openid, 'send_data': send_data})
        validator.validate()
        res = await wx_client.template_send(template_id=template_id, openid=openid, url=url, access_token=access_token,
                                            **send_data)
        self.do_success(res)


@route(r'/api/weixin/service_center/code_authorize/$')
class WeiXinServerCodeAuthorize(WebHandler):
    """通过code获取网页授权access_token"""
    async def get(self, *args, **kwargs):
        code = self.get_param('code')
        app_id = self.get_param('app_id')
        app_secret = self.get_param('app_secret')
        res = await wx_client.code_authorize(code=code, app_id=app_id, app_secret=app_secret)
        self.do_success(res)


@route(r'/api/weixin/service_center/get_web_user_info/$')
class WeiXinServerWebUserInfo(WebHandler):
    """获取网页认证用户信息"""
    async def get(self, *args, **kwargs):
        openid = self.get_param('openid')
        access_token = self.get_param('access_token')

        validator = UserInfoValidator({'openid': openid, 'access_token': access_token})
        validator.validate()

        res = await wx_client.get_web_user_info(openid=openid, access_token=access_token)
        self.do_success(res)


@route(r'/api/weixin/service_center/get_user_info/$')
class WeiXinServerUserInfo(WebHandler):
    """获取基础认证用户信息"""
    async def get(self, *args, **kwargs):
        openid = self.get_param('openid')
        access_token = self.get_param('access_token')

        validator = UserInfoValidator({'openid': openid, 'access_token': access_token})
        validator.validate()

        res = await wx_client.get_user_info(openid=openid, access_token=access_token)
        self.do_success(res)


@route(r'/api/weixin/service_center/temporary_qr_code/$')
class WeiXinServerTemporaryQrCode(WebHandler):
    """获取临时二维码"""
    async def post(self, *args, **kwargs):
        action_name = self.data.get('action_name')
        scene_id = self.data.get('scene_id')
        expired_seconds = self.get_param('expired_seconds', 7*24*60*60)
        access_token = self.data.get('access_token')

        validator = TemporaryQrCodeValidator({'action_name': action_name, 'expired_seconds': expired_seconds})
        validator.validate()
        res = await wx_client.get_temporary_qr_code(action_name=action_name,
                                                    scene_id=scene_id,
                                                    expired_seconds=expired_seconds,
                                                    access_token=access_token)
        self.do_success(res)


@route(r'/api/weixin/service_center/forever_qr_code/$')
class WeiXinServerForeverQrCode(WebHandler):
    """获取永久二维码"""
    async def post(self, *args, **kwargs):
        action_name = self.data.get('action_name')
        scene_id = self.data.get('scene_id')
        access_token = self.data.get('access_token')

        validator = ForeverQrCodeValidator({'action_name': action_name})
        validator.validate()
        res = await wx_client.get_forever_qr_code(action_name=action_name,
                                                  scene_id=scene_id,
                                                  access_token=access_token)
        self.do_success(res)
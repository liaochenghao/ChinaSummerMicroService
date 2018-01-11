from core.routes import route
from core.webbase import WebHandler
from service.wexin.client import wx_client
from api.weixin.validators import TextMessageValidator, TemplateMessageValidator


@route(r'/api/weixin/service_center/access_token/$')
class WeXinServerAccessToken(WebHandler):
    """
    微信服务access_token
    """

    def get(self, *args, **kwargs):
        access_token = wx_client.get_valid_access_token
        self.do_success({'access_token': access_token})


@route(r'/api/weixin/service_center/send_text_message/$')
class WeXinServerTextMessage(WebHandler):
    """
    通过客服消息接口，给用户发送文本消息
    """
    def post(self, *args, **kwargs):
        openid = self.data.get('openid')
        content = self.data.get('content')
        access_token = self.data.get('access_token', None)

        validator = TextMessageValidator({'openid': openid, 'content': content})
        validator.validate()
        res = wx_client.send_text_message(openid=openid, content=content, access_token=access_token)
        self.do_success(res)


@route(r'/api/weixin/service_center/send_template_message/$')
class WeiXinServerTemplateMessage(WebHandler):
    """
    发送模板消息
    """
    def post(self, *args, **kwargs):
        template_id = self.data.get('template_id')
        openid = self.data.get('openid')
        send_data = self.data.get('send_data')
        url = self.data.get('url')
        access_token = self.data.get('access_token', None)

        validator = TemplateMessageValidator({'template_id': template_id, 'openid': openid, 'send_data': send_data})
        validator.validate()
        res = wx_client.template_send(template_id=template_id, openid=openid, url=url, access_token=access_token,
                                      **send_data)
        self.do_success(res)
### 署校联盟微服务，为暑校学生系统，留声小程序，署校联盟服务中心微信公众号提供认证等相关服务

#### 测试服务地址
- http://42.51.8.152:7070


### 数据返回格式

**统一为 `json` 格式**:
```
    {
        "code": 0,
        "msg": "success",
        "data": {
            ... // 数据内容
        }
        field_name: ""
    }
```
- code `int` 0为成功，非0为失败 (code=401表示未登录)
- msg `string` 成功或失败的消息
- data `dict` 返回的数据内容
- field_name: `str`  code为非0状态时，报错字段


#### 1.学生系统接口
- [验证ticket有效性](docs/stu_system/ticket_authorize.md)
- [根据用户创建ticket](docs/stu_system/create_ticket.md)
- [删除ticket](docs/stu_system/delete_ticket.md)


#### 2.留声小程序接口
- [验证ticket有效性](docs/ugc_system/ticket_authorize.md)
- [根据用户创建ticket](docs/ugc_system/create_ticket.md)
- [删除ticket](docs/ugc_system/delete_ticket.md)


#### 3.服务中心微信公众号接口
- [获取access_token](docs/weixin/get_access_token.md)
- [发送文本消息](docs/weixin/send_text_message.md)
- [发送模板消息](docs/weixin/send_template_message.md)
- [code网页认证](docs/weixin/code_authorize.md)
- [获取网页认证用户信息](docs/weixin/get_web_user_info.md)
- [获取基础用户信息](docs/weixin/get_user_info.md)
- [生成临时二维码](docs/weixin/temporary_qr_code.md)
- [生成永久二维码](docs/weixin/forever_qr_code.md)

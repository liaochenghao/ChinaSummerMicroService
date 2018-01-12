###  发送文本消息

**请求地址**:
```
    POST    /api/weixin/service_center/send_text_message/
```

**请求参数**:
```
{
    "openid": str   用户openid  必填
    "content": str  发送内容  必填
    "access_token":  access_token  选填  若access_token为空，则默认以署校联盟服务中心发送给用户
}
```

**成功返回**：
```
{
    "code": 0,
    "msg": "success",
    "data": {
        "errcode": 0,
        "errmsg": "ok"
    }
}
```

**失败返回**：
```

```
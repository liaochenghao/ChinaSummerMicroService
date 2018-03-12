### code网页认证

**请求地址**:
```
    GET         /api/weixin/service_center/code_authorize/
```

**请求参数**:
```
    {
        "code": str 必填,
        "app_id": str   选填
        "app_secret": str   选填
    }
```
app_id, app_secret为选填参数
如果不填，则默认使用学生系统所在微信公众号进行认真，
调用此接口前需要确认要请求的微信公众号
```
```

**成功返回**：
```
{
    "access_token":"ACCESS_TOKEN",
    "expires_in":7200,
    "refresh_token":"REFRESH_TOKEN",
    "openid":"OPENID",
    "scope":"SCOPE"
}
```

**失败返回**：
```

```
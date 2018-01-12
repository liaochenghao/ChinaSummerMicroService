### code网页认证

**请求地址**:
```
    GET         /api/weixin/service_center/code_authorize/
```

**请求参数**:
```
    {
        "code": str 必填
    }
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
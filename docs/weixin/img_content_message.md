### 发送图文消息

**请求地址**:
```
    POST     /api/weixin/service_center/img_content_send/
```

**请求参数**:
```
{
	"access_token":  str  非必填
	"openid": str   必填
	"articles": list    必填
}
```
articles: 参数类型
{
    "title":"Happy Day",
    "description":"Is Really A Happy Day",
    "url":"URL",
    "picurl":"PIC_URL"
}
```
```

**成功返回**：
```
{
    "code": 0,
    "msg": "success",
    "data": {
    }
}
```

**失败返回**：
```

```
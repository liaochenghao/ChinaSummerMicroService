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
        "ticket": "gQF_8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyNTRfV3hKMEdjMGoxbzNveE5xMVcAAgSDXVhaAwSAOgkA",
        "expire_seconds": 604800,
        "url": "http://weixin.qq.com/q/0254_WxJ0Gc0j1o3oxNq1W",
        "qr_img_url": "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=gQF_8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyNTRfV3hKMEdjMGoxbzNveE5xMVcAAgSDXVhaAwSAOgkA"
    }
}
```

**失败返回**：
```

```
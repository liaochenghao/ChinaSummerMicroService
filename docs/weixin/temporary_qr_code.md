### 生成临时二维码

**请求地址**:
```
    GET     /api/weixin/service_center/temporary_qr_code/
```

**请求参数**:
```
{
	"expired_time": int  必填  二维码有效时间, 默认为7*24*60*60秒
	"action_name":   str  必填  二维码类型  QR_SCENE或QR_STR_SCENE
	"scene_id":      int或str  必填 场景值  当为QR_SCENE为int，否则为str
	"access_token":  str  非必填
}
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
### 生成永久二维码

**请求地址**:
```
    GET     /api/weixin/service_center/forever_qr_code/
```

**请求参数**:
```
{
	"action_name":   str  必填  二维码类型  QR_LIMIT_SCENE或QR_LIMIT_STR_SCENE
	"scene_id":      int或str  必填 场景值  当为QR_LIMIT_SCENE为int，否则为str
	"access_token":  str  非必填
}
```

**成功返回**：
```
{
    "code": 0,
    "msg": "success",
    "data": {
        "ticket": "gQEp8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyTFQ1b3gwMEdjMGoxMDAwMGcwM3IAAgRiX1haAwQAAAAA",
        "url": "http://weixin.qq.com/q/02LT5ox00Gc0j10000g03r",
        "qr_img_url": "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=gQEp8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyTFQ1b3gwMEdjMGoxMDAwMGcwM3IAAgRiX1haAwQAAAAA"
    }
}
```

**失败返回**：
```

```
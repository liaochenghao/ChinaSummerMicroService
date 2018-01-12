###  获取基础的用户信息

**请求地址**:
```
    GET     /api/weixin/service_center/get_user_info/
```

**请求参数**:
```
{
    "openid": str   必填,
    "access_token": str 非必填
}
```

**成功返回**：
```
{
    "code": 0,
    "msg": "success",
    "data": {
        "subscribe": 1,
        "openid": "oAKoA0_Pps0xXJSuRZPtkA_NI3jg",
        "nickname": "邱雷",
        "sex": 1,
        "language": "zh_CN",
        "city": "成都",
        "province": "四川",
        "country": "中国",
        "headimgurl": "http://wx.qlogo.cn/mmopen/dx4Y70y9XcvagTSvzSjnJicORylW6hLO91hA2kuyNm8iaC5gekve0I7yEF72umb9pkWBXTSF8BluxbaTicwlWTfvA/132",
        "subscribe_time": 1515523205,
        "unionid": "ooYUms6S7PaAH3aIzFVZtXP-Ikb0",
        "remark": "",
        "groupid": 0,
        "tagid_list": []
    }
}
```

**失败返回**：
```

```